from playwright.sync_api import expect, sync_playwright

BASE_URL = "https://practicesoftwaretesting.com/"


def test_browse_category(page):
    page.goto(BASE_URL)
    page.get_by_role("button", name=" Categories").click()
    page.get_by_role("link", name="Hand Tools").click()

    assert page.title() == "Hand Tools - Practice Software Testing - Toolshop - v5.0"
    print(page.title())
    
    product_count = page.locator('[data-test="product-name"]').count()
    if product_count > 0:
        print("PASS: Hand Tools category with one product")
        for i in range(product_count):
            product_name = page.locator('[data-test="product-name"]').nth(i).inner_text()
            if (product_name.strip() == ""):
                print(f"FAIL: Product {i + 1} is empty")
            else:
                print(f"Product {i + 1}: {product_name}")

def test_product_details(page):
    page.goto(BASE_URL)

    page.get_by_role("button", name="Categories").click()
    page.get_by_role("link", name="Hand Tools").click()

    products = page.locator('a.card[data-test^="product-"]')
    products.first.wait_for()

    expected_name = products.first.locator("h5").inner_text().strip()
    products.first.click()

    actual_name = page.locator(
        'h1[data-test="product-name"]'
    ).inner_text().strip()

    assert actual_name == expected_name, (
        f"Expected product name '{expected_name}', but got '{actual_name}'"
    )

    price = page.locator('[data-test="unit-price"]')
    assert price.is_visible(), "Expected product price to be visible"
    assert price.inner_text().strip(), "Expected product price not to be empty"

    add_to_cart = page.locator("#btn-add-to-cart")
    assert add_to_cart.is_visible(), "Expected Add to Cart button to be visible"


def test_add_to_cart(page):
    """Test 3: Add first Hand Tools product to cart and verify cart."""
    page.goto(BASE_URL)
    page.locator('[data-test="nav-categories"]').click()
    page.locator('[data-test="nav-hand-tools"]').click()

    first_product = page.locator('[data-test="product-name"]').first
    product_name = first_product.inner_text().strip()
    first_product.click()

    price_text = page.locator('[data-test="unit-price"]').inner_text().strip()
    page.locator('[data-test="add-to-cart"]').click()

    cart_count = page.locator('[data-test="cart-quantity"]')
    expect(cart_count).to_have_text("1")

    page.locator('[data-test="nav-cart"]').click()

    cart_item_name = page.locator('[data-test="product-title"]').first.inner_text().strip()
    assert product_name in cart_item_name, \
        f"Expected '{product_name}' in cart, got '{cart_item_name}'"

    cart_qty = page.locator('[data-test="cart-quantity"]').first
    expect(cart_qty).to_have_value("1")

    cart_total = page.locator('[data-test="cart-total"]').inner_text().strip()
    assert price_text in cart_total or price_text.replace("$", "") in cart_total, \
        f"Expected price {price_text} in cart total {cart_total}"
    print("PASS: test_add_to_cart")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        test_browse_category(page)
        page.wait_for_timeout(3000)
        browser.close()
        
        
if __name__ == "__main__":
    main()
