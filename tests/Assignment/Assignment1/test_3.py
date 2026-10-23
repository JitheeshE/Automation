 #Scenario 3: DemoWebShop – Select Product by Price

from playwright.sync_api import sync_playwright, expect

def test_demowebshop_select_product_by_price():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demowebshop.tricentis.com/")
        page.wait_for_load_state("domcontentloaded")

        page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()

        product_price = "$50.00"

        product = page.locator("//div[contains(@class,'product-item')]""[.//span[contains(@class,'price') and normalize-space()='{product_price}']]")
        
        expect(product).to_be_visible()

        product_name = product.locator(".//h2/a").inner_text().strip()

        print("Product Name:", product_name)
        print("Product Price:", product_price)

        add_to_cart = product.locator("xpath=.//input[contains(@value,'Add to cart')]")

        expect(add_to_cart).to_be_visible()

        add_to_cart.click()

        page.locator("//span[@class='cart-label']").click()

        expect(page.locator(f"//a[normalize-space()='{product_name}']")).to_be_visible()

        print(f"PASS: {product_name} "f"({product_price}) added to cart successfully.")

        browser.close()