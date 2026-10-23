#Scenario 1: DemoWebShop – Product Name to Add to Cart

from playwright.sync_api import sync_playwright, expect

def test_demowebshop_add_book_to_cart():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demowebshop.tricentis.com/")
        page.wait_for_load_state("domcontentloaded")

        page.locator("//ul[@class='top-menu']//a[contains(text(),'Books')]").click()

        product_name = "Health Book"

        product = page.locator(f"//div[contains(@class,'product-item')]"f"[.//h2/a[normalize-space()='{product_name}']]")

        expect(product).to_be_visible()

        add_to_cart = product.locator("xpath=.//input[@value='Add to cart']")

        add_to_cart.click()

        page.locator("//span[@class='cart-label' and normalize-space()='Shopping cart']").click()

        cart_product = page.locator(f"xpath=//a[normalize-space()='{product_name}']")
        expect(cart_product).to_be_visible()

        print(f"'{product_name}' has been successfully added to the cart.")

        browser.close()
        
        