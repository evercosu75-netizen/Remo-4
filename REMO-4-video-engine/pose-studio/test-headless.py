"""Uji ulang headless — pose studio REMO 4 (sudah diperbaiki).
Folder: ~/workspace/remo-4/pose-studio/studio-anatomi-pose.html
Basis: pose-studio-test/test-headless.py, ditambah pengukuran sendi
(salam / tolak pinggang / berpikir), toggle otot, CoG, dan ketahanan
saat CDN Lucide gagal total."""
import json, pathlib, subprocess, sys, time, socket, urllib.request
from playwright.sync_api import sync_playwright

BASE = pathlib.Path.home() / "workspace" / "remo-4" / "pose-studio"
SHOTS = BASE / "shots"; SHOTS.mkdir(parents=True, exist_ok=True)
EXP = BASE / "exports"; EXP.mkdir(parents=True, exist_ok=True)

def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p

def cdn_proxy(route, report, block_lucide=False):
    url = route.request.url
    if block_lucide and "unpkg.com" in url:
        route.abort()
        return
    if any(h in url for h in ["cdn.tailwindcss.com", "unpkg.com", "fonts.googleapis.com", "fonts.gstatic.com"]):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                route.fulfill(status=200, body=resp.read(),
                              content_type=resp.headers.get("Content-Type", "application/octet-stream"))
        except Exception as e:
            report["failed_requests"].append(f"CDN-PROXY {url} :: {e}")
            route.abort()
    else:
        route.continue_()

PORT = free_port()
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"], cwd=str(BASE))
time.sleep(1.0)

report = {"console": [], "pageerrors": [], "failed_requests": [], "requests": []}
try:
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        ctx = b.new_context(viewport={"width": 1600, "height": 1000}, accept_downloads=True)
        pg = ctx.new_page()
        pg.on("console", lambda m: report["console"].append(f"{m.type}: {m.text}"))
        pg.on("pageerror", lambda e: report["pageerrors"].append(str(e)))
        pg.on("requestfailed", lambda r: report["failed_requests"].append(f"{r.url} :: {r.failure}"))
        pg.route("**/*", lambda route: cdn_proxy(route, report))
        pg.goto(f"http://127.0.0.1:{PORT}/studio-anatomi-pose.html")
        pg.wait_for_timeout(4000)

        # --- 1. libs ---
        report["libs"] = pg.evaluate("""() => ({
          tailwind: typeof window.tailwind !== 'undefined',
          lucide: typeof window.lucide !== 'undefined',
          lucideIconsRendered: document.querySelectorAll('svg.lucide').length,
          charRendered: document.querySelectorAll('#characterContainer > g').length,
          skeletonJoints: document.querySelectorAll('#layerSkeleton .joint-node').length,
          guideRows: document.querySelectorAll('#layerProportions .guide-row').length,
          presetButtons: document.querySelectorAll('.preset-btn').length,
          bodyFont: getComputedStyle(document.body).fontFamily.slice(0,60),
        })""")

        def joints():
            return pg.evaluate("""() => {
              const out = {};
              document.querySelectorAll('#layerSkeleton .joint-node').forEach(n => {
                const c = n.querySelector('circle');
                out[n.getAttribute('data-joint-name')] = [+c.getAttribute('cx'), +c.getAttribute('cy')];
              });
              return out;
            }""")

        # --- 2. Head vs Canon (default netral pria) ---
        head = pg.evaluate("""() => {
          const cc = document.getElementById('characterContainer');
          const headG = cc.querySelector(':scope > g:last-child');
          const bb = headG.getBBox();
          const cbb = cc.getBBox();
          const guideYs = [...document.querySelectorAll('#layerProportions line')].map(l=>+l.getAttribute('y1'));
          return {headBBox: {x: +bb.x.toFixed(1), y: +bb.y.toFixed(1), w: +bb.width.toFixed(1), h: +bb.height.toFixed(1)},
                  headTop: +bb.y.toFixed(1), headBottom: +(bb.y + bb.height).toFixed(1),
                  charBBox: {x: +cbb.x.toFixed(1), y: +cbb.y.toFixed(1), w: +cbb.width.toFixed(1), h: +cbb.height.toFixed(1)},
                  charTop: +cbb.y.toFixed(1), charBottom: +(cbb.y + cbb.height).toFixed(1),
                  guideYs: guideYs.slice(0,9)};
        }""")
        head["joints"] = joints()
        report["head_vs_canon_default"] = head
        pg.screenshot(path=str(SHOTS / "01-default-pria-batik-senyum.png"))

        # --- 3. Slider limits + semua preset: state vs slider (clamp?) + posisi sendi ---
        report["slider_limits"] = pg.evaluate("""() => {
          const out = {};
          ['headAngle','chestAngle','pelvisAngle','armLAngle','forearmLAngle','armRAngle','forearmRAngle','thighLAngle','kneeLAngle','thighRAngle','kneeRAngle'].forEach(k=>{
            const el = document.getElementById('param_'+k);
            out[k] = {min:+el.min, max:+el.max, value:+el.value};
          });
          return out;
        }""")
        preset_results = {}
        for pid in ["netral", "salam", "menyapa", "berjalan", "tolakpinggang", "berpikir", "santai"]:
            pg.click(f".preset-btn[data-pose-id='{pid}']")
            pg.wait_for_timeout(300)
            r = pg.evaluate("""() => {
              const out = {statePose: {...state.pose}, sliders: {}, displays: {}};
              Object.keys(state.pose).forEach(k=>{
                const el = document.getElementById('param_'+k);
                out.sliders[k] = +el.value;
                out.displays[k] = document.getElementById('val_'+k).textContent;
              });
              return out;
            }""")
            r["joints"] = joints()
            r["clamped"] = [k for k in r["statePose"] if r["statePose"][k] != r["sliders"][k]]
            preset_results[pid] = r
        report["preset_clicks"] = preset_results
        pg.click(".preset-btn[data-pose-id='salam']"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(SHOTS / "02-preset-salam-santun.png"))
        pg.click(".preset-btn[data-pose-id='tolakpinggang']"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(SHOTS / "03-preset-tolak-pinggang.png"))
        pg.click(".preset-btn[data-pose-id='berpikir']"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(SHOTS / "07-preset-berpikir.png"))

        # --- 4. Wanita + kebaya + semangat ---
        pg.click(".preset-btn[data-pose-id='netral']"); pg.wait_for_timeout(300)
        pg.click("#btnCharFemale"); pg.wait_for_timeout(300)
        pg.click("[data-expression='semangat']"); pg.wait_for_timeout(300)
        fem = pg.evaluate("""() => ({gender: state.gender, outfit: state.outfit, expr: state.expression,
          headTop: +document.getElementById('characterContainer').querySelector(':scope > g:last-child').getBBox().y.toFixed(1),
          jointsHead: document.querySelector('#layerSkeleton .joint-node circle').getAttribute('cy')})""")
        report["female_semangat"] = fem
        pg.screenshot(path=str(SHOTS / "04-wanita-kebaya-semangat.png"))

        # --- 5. Toggle Anatomi Otot (dengan outfit kasual dulu: harus TIDAK tertimpa) ---
        pg.click("[data-outfit='casual']"); pg.wait_for_timeout(300)
        before = pg.evaluate("""() => ({outfit: state.outfit, musclesHidden: document.getElementById('layerMuscles').classList.contains('hidden'),
          musclesChildren: document.getElementById('layerMuscles').children.length})""")
        pg.click("#toggleMuscles"); pg.wait_for_timeout(400)
        after_on = pg.evaluate("""() => ({outfit: state.outfit, musclesHidden: document.getElementById('layerMuscles').classList.contains('hidden'),
          musclesChildren: document.getElementById('layerMuscles').children.length,
          toggleClass: document.getElementById('toggleMuscles').className})""")
        pg.screenshot(path=str(SHOTS / "05-toggle-anatomi-otot.png"))
        pg.click("#toggleMuscles"); pg.wait_for_timeout(300)
        after_off = pg.evaluate("""() => ({outfit: state.outfit, musclesHidden: document.getElementById('layerMuscles').classList.contains('hidden'),
          musclesChildren: document.getElementById('layerMuscles').children.length})""")
        report["toggle_muscles"] = {"before": before, "after_on": after_on, "after_off": after_off}

        # --- 6. Toggle Garis Titik Berat (CoG) ---
        pg.click("#toggleGravity"); pg.wait_for_timeout(300)
        cog = pg.evaluate("""() => {
          const line = document.getElementById('cogLine'), pt = document.getElementById('cogPoint');
          const lbl = document.getElementById('cogLabel');
          return {gravityHidden: document.getElementById('layerGravity').classList.contains('hidden'),
                  lineX1: line.getAttribute('x1'), lineX2: line.getAttribute('x2'),
                  pointCx: pt.getAttribute('cx'), pointCy: pt.getAttribute('cy'),
                  labelX: lbl.getAttribute('x'), labelY: lbl.getAttribute('y')};
        }""")
        report["toggle_gravity"] = cog
        pg.screenshot(path=str(SHOTS / "06-toggle-garis-titik-berat.png"))
        pg.click("#toggleGravity"); pg.wait_for_timeout(200)

        # --- 7. Export SVG + PNG ---
        with pg.expect_download() as dl1:
            pg.click("#btnExportSvg")
        d1 = dl1.value
        p1 = EXP / ("export-" + d1.suggested_filename)
        d1.save_as(str(p1))
        report["export_svg"] = {"file": str(p1), "size": p1.stat().st_size,
                                "starts": p1.read_text(errors="ignore")[:120]}
        with pg.expect_download() as dl2:
            pg.click("#btnExportPng")
            pg.wait_for_timeout(1500)
        d2 = dl2.value
        p2 = EXP / ("export-" + d2.suggested_filename)
        d2.save_as(str(p2))
        report["export_png"] = {"file": str(p2), "size": p2.stat().st_size,
                                "header": p2.read_bytes()[:8].hex()}

        # --- 8. Ketahanan CDN: blokir total unpkg/lucide, halaman harus tetap jalan ---
        ctx2 = b.new_context(viewport={"width": 1600, "height": 1000})
        pg2 = ctx2.new_page()
        rep2 = {"pageerrors": [], "console": []}
        pg2.on("pageerror", lambda e: rep2["pageerrors"].append(str(e)))
        pg2.on("console", lambda m: rep2["console"].append(f"{m.type}: {m.text}"))
        pg2.route("**/*", lambda route: cdn_proxy(route, report, block_lucide=True))
        pg2.goto(f"http://127.0.0.1:{PORT}/studio-anatomi-pose.html")
        pg2.wait_for_timeout(4000)
        rep2["renders"] = pg2.evaluate("""() => ({
          skeletonJoints: document.querySelectorAll('#layerSkeleton .joint-node').length,
          charGroups: document.querySelectorAll('#characterContainer > g').length,
          lucideDefined: typeof window.lucide !== 'undefined',
          iconsRendered: document.querySelectorAll('svg.lucide').length,
        })""")
        pg2.screenshot(path=str(SHOTS / "08-tanpa-lucide-cdn.png"))
        report["lucide_blocked"] = rep2
        b.close()
finally:
    srv.terminate()

(BASE / "test-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
print(json.dumps(report, indent=2, ensure_ascii=False))
