"""Smoke test: load the catalog and every course, click through all steps at phone width,
and fail on JavaScript errors or horizontal page overflow."""
import pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
pages = [ROOT / "index.html"] + sorted(ROOT.glob("courses/*/index.html"))
CLICKABLE = [".opt", ".link", ".evbtn", ".sitem .seg button", ".stage", ".reveal"]
failed = False

with sync_playwright() as p:
    browser = p.chromium.launch()
    for path in pages:
        page = browser.new_page(viewport={"width": 400, "height": 900})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(path.as_uri())
        page.wait_for_timeout(300)
        steps = 0
        if page.query_selector("#next"):
            # walk until the course wraps back to the first step
            for steps in range(1, 400):
                for sel in CLICKABLE:
                    el = page.query_selector(sel)
                    if el and el.is_enabled():
                        el.click()
                page.click("#next")
                if page.query_selector("#back[disabled]"):
                    break
        width = page.evaluate("document.documentElement.scrollWidth")
        ok = not errors and width <= 400
        failed |= not ok
        print(f"{'PASS' if ok else 'FAIL'}  {path.relative_to(ROOT)}  steps={steps}  width={width}  errors={errors}")
        page.close()
    browser.close()

sys.exit(1 if failed else 0)
