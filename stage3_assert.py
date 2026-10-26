from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://practicesoftwaretesting.com"
SEARCH_TERM = "pliers"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(BASE_URL)
    page.locator('[data-test="search-query"]').fill(SEARCH_TERM)
    page.locator('[data-test="search-submit"]').click()

    first_product = page.locator('[data-test="product-name"]').first


    expect(first_product).to_contain_text(SEARCH_TERM, ignore_case=True)


    print(f"PASS: '{SEARCH_TERM}' found products")

    browser.close()
