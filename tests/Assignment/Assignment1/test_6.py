# Scenario 6: Amazon – Search Results

from playwright.sync_api import sync_playwright, expect

def test_amazon_search_result_book():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in/")
        page.wait_for_load_state("domcontentloaded")

        search_box = page.locator("//input[@id='twotabsearchtextbox']")  
        
        search_box.fill("The Alchemist")

        page.locator("//input[@id='nav-search-submit-button']").click()

        page.wait_for_load_state("domcontentloaded")

        book_title = "The Alchemist"

        product = page.locator(f"//div[@data-component-type='s-search-result']"f"[.//h2//span[contains(normalize-space(), '{book_title}')]]")

        expect(product).to_be_visible()

        actual_title = product.locator(".//h2//span").inner_text().strip()

        print("\nBook Title:", actual_title)

        price = product.locator(".//span[contains(@class,'a-price')]""//span[contains(@class,'a-offscreen')]")

        if price.count() > 0:
            product_price = price.first.inner_text().strip()
            print("Price:", product_price)
        else:
            print("Price is not available.")

        add_to_cart = product.locator(".//button[contains(.,'Add to cart')]""|.//input[contains(@value,'Add to Cart')]")

        if add_to_cart.count() > 0:

            expect(add_to_cart.first).to_be_visible()

            add_to_cart.first.click()

            print("Add to Cart clicked successfully.")

        else:

            print("Add to Cart is not available in this search result.")

        browser.close()