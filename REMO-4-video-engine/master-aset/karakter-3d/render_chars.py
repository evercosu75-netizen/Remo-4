"""Render PNG transparan per kostum/pose dari render.html (Three.js lokal)."""
import pathlib, sys, subprocess, time, socket
from playwright.sync_api import sync_playwright

def free_port():
    s=socket.socket(); s.bind(("127.0.0.1",0)); p=s.getsockname()[1]; s.close(); return p

here = pathlib.Path(__file__).parent.resolve()
raw = here / "renders" / "raw"; raw.mkdir(parents=True, exist_ok=True)
out = here / "renders"; out.mkdir(parents=True, exist_ok=True)

PORT = free_port()
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"], cwd=str(here))
time.sleep(1.0)
JOBS = [
    ("diver_m", "male", "diver_m", "swim"),
    ("diver_f", "female", "diver_f", "swim"),
    ("swim_teal", "male", "swim_teal", "stand"),
    ("swim_orange", "male", "swim_orange", "stand"),
    ("swim_aqua", "female", "swim_aqua", "stand"),
    ("swim_pink", "female", "swim_pink", "stand"),
    ("fisherman", "male", "fisherman", "stand"),
    ("miner", "male", "miner", "stand"),
    ("land_m", "male", "land_m", "stand"),
    ("land_f", "female", "land_f", "stand"),
    ("diver_shrug", "male", "diver_m", "shrug"),
]
only = sys.argv[1:] or None
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, char, costume, pose in JOBS:
        if only and name not in only:
            continue
        pg = b.new_page(viewport={"width": 800, "height": 1000})
        url = f"http://127.0.0.1:{PORT}/render.html?char={char}&costume={costume}&pose={pose}"
        pg.goto(url)
        pg.wait_for_function("window.__ready === true", timeout=15000)
        pg.wait_for_timeout(300)
        path = raw / f"{name}.png"
        pg.screenshot(path=str(path), omit_background=True)
        pg.close()
        print(name, 'saved', path)
    b.close()
srv.terminate()
print("done")
