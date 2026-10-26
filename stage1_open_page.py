from playwright.sync_api import sync_playwright

BASE_URL = "https://practicesoftwaretesting.com"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto(BASE_URL)
    print(page.title())

    page.wait_for_timeout(3000)

    browser.close()