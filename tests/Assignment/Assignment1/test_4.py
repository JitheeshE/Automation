 # Scenario 4: Amazon – Product Name and Price

from playwright.sync_api import sync_playwright, expect

def test_amazon_product_name_and_price():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in/")
        page.wait_for_load_state("domcontentloaded")

        search_box = page.locator("xpath=//input[@id='twotabsearchtextbox']")

        search_box.fill("Nothing Phone")

        page.locator("//input[@id='nav-search-submit-button']").click()

        page.wait_for_load_state("domcontentloaded")

        product_name = "Nothing Phone 2"

        product = page.locator(f"//div[@data-component-type='s-search-result']"f"[.//h2//span[normalize-space()='{product_name}']]")

        expect(product).to_be_visible()

        actual_product_name = product.locator(".//h2//span").inner_text().strip()

        price = product.locator(".//span[contains(@class,'a-price')]""//span[contains(@class,'a-offscreen')]")

        expect(price).to_be_visible()

        product_price = price.inner_text().strip()

        print("PRODUCT DETAILS")
        print("Product Name :", actual_product_name)
        print("Product Price:", product_price)
        browser.close()
        