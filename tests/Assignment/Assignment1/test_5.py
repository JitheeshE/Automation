# Scenario 5: DemoWebShop – Product Name and Rating

from playwright.sync_api import sync_playwright, expect

def test_demowebshop_product_name_and_rating():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demowebshop.tricentis.com/")
        page.wait_for_load_state("domcontentloaded")

        page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()

        product_name = "Health Book"

        product = page.locator(f"//div[contains(@class,'product-item')]"f"[.//h2/a[normalize-space()='{product_name}']]")

        expect(product).to_be_visible()

        actual_product_name = product.locator(".//h2/a").inner_text().strip()

        rating = product.locator(".//div[contains(@class,'rating')]")

        expect(rating).to_be_visible()

        rating_class = rating.get_attribute("class")

        print("PRODUCT DETAILS")
        print("Product Name :", actual_product_name)
        print("Rating Class :", rating_class)

        expect(product).to_contain_text(product_name)
        expect(rating).to_be_visible()

        print(f"PASS: '{actual_product_name}' and its rating "f"belong to the same product container.")

        browser.close()