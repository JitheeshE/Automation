# Scenario 7: DemoWebShop – Multiple Products

from playwright.sync_api import sync_playwright, expect


def test_demowebshop_multiple_products():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demowebshop.tricentis.com/")
        page.wait_for_load_state("domcontentloaded")

        page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()

        products = page.locator("//div[contains(@class,'product-item')]")

        expect(products.first).to_be_visible()

        product_count = products.count()

        for i in range(product_count):

            product = products.nth(i)

            product_name = product.locator(".//h2/a").inner_text().strip()

            print(f"{i + 1}. {product_name}")

        target_product_name = "Health Book"

        target_product = page.locator(f"//div[contains(@class,'product-item')]"f"[.//h2/a[normalize-space()='{target_product_name}']]")

        expect(target_product).to_be_visible()

        add_to_cart = target_product.locator(".//input[contains(@value,'Add to cart')]")

        expect(add_to_cart).to_be_visible()

        add_to_cart.click()

        print(f"\n'{target_product_name}'""added to cart." )

        page.locator("//span[@class='cart-label']").click()

        cart_product = page.locator(f"//a[normalize-space()='{target_product_name}']")

        expect(cart_product).to_be_visible()

        print(f'{target_product_name}'"is available in the cart.")

        browser.close()