# Scenario 9: DemoWebShop – Product Details

from playwright.sync_api import sync_playwright, expect

def test_demowebshop_product_details():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demowebshop.tricentis.com/")
        page.wait_for_load_state("domcontentloaded")

        page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()

        product_name = "Health Book"

        product_link = page.locator(f"//h2/a[normalize-space()='{product_name}']")

        expect(product_link).to_be_visible()

        product_link.click()

        page.wait_for_load_state("domcontentloaded")

        product_title = page.locator(f"//div[contains(@class,'product-name')]"f"//h1[normalize-space()='{product_name}']")

        expect(product_title).to_be_visible()

        print("PRODUCT DETAILS")
        print("Product Name :", product_title.inner_text().strip())

        price = page.locator("//div[contains(@class,'product-price')]""//span[contains(@class,'price')]")

        expect(price).to_be_visible()

        product_price = price.inner_text().strip()

        print("Product Price:", product_price)

        add_to_cart = page.locator("//input[contains(@value,'Add to cart')]" )

        expect(add_to_cart).to_be_visible()

        print("Add to Cart  : Available")

        add_to_cart.click()

        page.locator("//span[@class='cart-label']").click()

        cart_product = page.locator(f"//a[normalize-space()='{product_name}']")

        expect(cart_product).to_be_visible()

        print("Cart Status  : Product added successfully")

        browser.close()