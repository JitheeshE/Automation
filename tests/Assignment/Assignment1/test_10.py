# Scenario 10: Amazon – Select Product from Search Results

from playwright.sync_api import sync_playwright, expect

def test_amazon_select_product_from_search_results():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in/")
        page.wait_for_load_state("domcontentloaded")

        search_box = page.locator("//input[@id='twotabsearchtextbox']" )

        search_box.fill("Nothing Phone")

        page.locator("//input[@id='nav-search-submit-button']").click()

        page.wait_for_load_state("domcontentloaded")

        product_title = "Nothing Phone 2"

        product = page.locator(f"//div[@data-component-type='s-search-result']"f"[.//h2//span[contains(normalize-space(), '{product_title}')]]")

        expect(product).to_be_visible()

        print("SEARCH RESULT")

        title = product.locator(".//h2//span")

        expect(title).to_be_visible()

        actual_title = title.inner_text().strip()

        print("Product Title:", actual_title)

        image = product.locator(".//img[contains(@class,'s-image')]")

        expect(image).to_be_visible()

        print("Product Image: Available")

        price = product.locator(".//span[contains(@class,'a-price')]""//span[contains(@class,'a-offscreen')]")

        if price.count() > 0:

            product_price = price.first.inner_text().strip()

            print("Product Price:", product_price)

        else:

            print("Product Price: Not available")

        product_link = product.locator(".//h2/a")

        expect(product_link).to_be_visible()

        product_link.click()

        page.wait_for_load_state("domcontentloaded")

        details_title = page.locator("//span[@id='productTitle']")

        expect(details_title).to_be_visible()

        actual_details_title = details_title.inner_text().strip()

        print("PRODUCT DETAILS")
        print("Details Title:", actual_details_title)

        assert product_title.lower() in actual_details_title.lower()

        print("PASS: Correct product details displayed.")

        browser.close()