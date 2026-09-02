from playwright.sync_api import sync_playwright

URL = "https://wizyty.uml.lodz.pl/"

with 
sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    print("TITLE:", page.title())
    print("URL:", page.url)
    print("TEXT:")
    print(page.locator("body").inner_text()[:12000])

    page.screenshot(path="wizyty.png", full_page=True)

    browser.close()
