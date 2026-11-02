"""Uji ulang headless — pose studio REMO 4 SETELAH merge engine background.
Folder: ~/workspace/remo-4/pose-studio/studio-anatomi-pose.html
Menguji: 8 latar + 4 waktu + DoF, proporsi kepala tetap 7,5 kepala,
preset Salam/Tolak Pinggang tetap benar, 0 pageerror.
"""
import json, pathlib, subprocess, sys, time, socket, urllib.request
from playwright.sync_api import sync_playwright

BASE = pathlib.Path.home() / "workspace" / "remo-4" / "pose-studio"
SHOTS = BASE / "shots"; SHOTS.mkdir(parents=True, exist_ok=True)

def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p

def cdn_proxy(route, report):
    url = route.request.url
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

        def joints():
            return pg.evaluate("""() => {
              const out = {};
              document.querySelectorAll('#layerSkeleton .joint-node').forEach(n => {
                const c = n.querySelector('circle');
                out[n.getAttribute('data-joint-name')] = [+c.getAttribute('cx'), +c.getAttribute('cy')];
              });
              return out;
            }""")

        # --- 1. UI latar ada + render awal ---
        report["bg_ui"] = pg.evaluate("""() => ({
          bgCards: document.querySelectorAll('.bg-card-btn').length,
          bgIds: [...document.querySelectorAll('.bg-card-btn')].map(b => b.getAttribute('data-bg')),
          todBtns: document.querySelectorAll('.tod-btn').length,
          dofBtn: !!document.getElementById('btnToggleDof'),
          layerBackground: !!document.getElementById('layerBackground'),
          dofFilter: !!document.getElementById('dofFilter'),
          bgState: state.background, todState: state.timeOfDay, dofState: state.enableDof,
          bgChars: document.getElementById('layerBackground').innerHTML.length,
          charGroups: document.querySelectorAll('#characterContainer > g').length,
          skeletonJoints: document.querySelectorAll('#layerSkeleton .joint-node').length,
        })""")

        # --- 2. Kepala vs panduan (default, latar candi senja) ---
        head = pg.evaluate("""() => {
          const cc = document.getElementById('characterContainer');
          const headG = cc.querySelector(':scope > g:last-child');
          const bb = headG.getBBox();
          const cbb = cc.getBBox();
          return {headTop: +bb.y.toFixed(1), headBottom: +(bb.y + bb.height).toFixed(1),
                  charTop: +cbb.y.toFixed(1), charBottom: +(cbb.y + cbb.height).toFixed(1),
                  joints: {}};
        }""")
        head["joints"] = joints()
        report["head_vs_canon_merged"] = head

        # --- 3. Siklus 8 latar ---
        bg_results = {}
        for bg in ["candi", "gadang", "sawah", "pantai", "jakarta", "blueprint", "cyclorama", "transparan"]:
            pg.click(f".bg-card-btn[data-bg='{bg}']")
            pg.wait_for_timeout(250)
            bg_results[bg] = pg.evaluate("""() => ({
              stateBg: state.background,
              chars: document.getElementById('layerBackground').innerHTML.length,
              charGroups: document.querySelectorAll('#characterContainer > g').length,
            })""")
        report["background_cycle"] = bg_results

        # --- 4. Siklus 4 waktu ---
        tod_results = {}
        for tod in ["pagi", "siang", "senja", "malam"]:
            pg.click(f".tod-btn[data-tod='{tod}']")
            pg.wait_for_timeout(250)
            tod_results[tod] = pg.evaluate("""() => ({
              stateTod: state.timeOfDay,
              chars: document.getElementById('layerBackground').innerHTML.length,
            })""")
        report["tod_cycle"] = tod_results

        # --- 5. DoF di latar sawah + screenshot ---
        pg.click(".bg-card-btn[data-bg='sawah']"); pg.wait_for_timeout(250)
        pg.click(".tod-btn[data-tod='siang']"); pg.wait_for_timeout(250)
        dof_before = pg.evaluate("""() => {
          const g = document.querySelector('#layerBackground #sceneryGroup');
          return {hasSceneryGroup: !!g, filter: g ? g.getAttribute('filter') : null, dofState: state.enableDof};
        }""")
        pg.click("#btnToggleDof"); pg.wait_for_timeout(400)
        dof_after = pg.evaluate("""() => {
          const g = document.querySelector('#layerBackground #sceneryGroup');
          return {hasSceneryGroup: !!g, filter: g ? g.getAttribute('filter') : null, dofState: state.enableDof,
                  btnText: document.getElementById('btnToggleDof').textContent.trim()};
        }""")
        report["dof_sawah"] = {"before": dof_before, "after": dof_after}
        pg.screenshot(path=str(SHOTS / "09-latar-sawah-dof-aktif.png"))
        pg.click("#btnToggleDof"); pg.wait_for_timeout(250)  # matikan lagi

        # --- 6. Latar candi senja + screenshot ---
        pg.click(".bg-card-btn[data-bg='candi']"); pg.wait_for_timeout(250)
        pg.click(".tod-btn[data-tod='senja']"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(SHOTS / "10-latar-candi-senja.png"))

        # --- 7. Preset Salam di atas latar candi + Tolak Pinggang ---
        pg.click(".preset-btn[data-pose-id='salam']"); pg.wait_for_timeout(400)
        salam = pg.evaluate("""() => {
          const out = {statePose: {...state.pose}, sliders: {}};
          Object.keys(state.pose).forEach(k => { out.sliders[k] = +document.getElementById('param_'+k).value; });
          return out;
        }""")
        salam["joints"] = joints()
        salam["clamped"] = [k for k in salam["statePose"] if salam["statePose"][k] != salam["sliders"][k]]
        report["salam_on_background"] = salam
        pg.screenshot(path=str(SHOTS / "11-preset-salam-di-latar-candi.png"))
        pg.click(".preset-btn[data-pose-id='tolakpinggang']"); pg.wait_for_timeout(400)
        tp = pg.evaluate("""() => {
          const out = {statePose: {...state.pose}, sliders: {}};
          Object.keys(state.pose).forEach(k => { out.sliders[k] = +document.getElementById('param_'+k).value; });
          return out;
        }""")
        tp["joints"] = joints()
        tp["clamped"] = [k for k in tp["statePose"] if tp["statePose"][k] != tp["sliders"][k]]
        report["tolakpinggang_on_background"] = tp

        # --- 8. Bonus: pantai malam ---
        pg.click(".preset-btn[data-pose-id='netral']"); pg.wait_for_timeout(250)
        pg.click(".bg-card-btn[data-bg='pantai']"); pg.wait_for_timeout(250)
        pg.click(".tod-btn[data-tod='malam']"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(SHOTS / "12-latar-pantai-malam.png"))

        b.close()
finally:
    srv.terminate()

(BASE / "test-merge-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
print(json.dumps(report, indent=2, ensure_ascii=False))
