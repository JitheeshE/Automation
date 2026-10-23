# Scenario 8: Amazon – Navigation Menu Subcategories

from playwright.sync_api import sync_playwright, expect

def test_amazon_navigation_subcategories():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in/")
        page.wait_for_load_state("domcontentloaded")

        page.locator("//a[@id='nav-hamburger-menu']").click()

        heading_name = "Digital Content & Devices"

        heading = page.locator(f"//div[@id='hmenu-content']"f"//*[self::div or self::a]"f"[normalize-space()='{heading_name}']")

        expect(heading).to_be_visible()

        print("\nMain Heading:", heading_name)

        heading_container = heading.locator("..")

        subcategories = heading_container.locator(".//a[contains(@class,'hmenu-item')]")

        count = subcategories.count()

        print("SUB CATEGORIES")
  
        for i in range(count):

            subcategory = subcategories.nth(i).inner_text().strip()

            if subcategory:
                print(f"{i + 1}. {subcategory}")

        required_subcategory = "Amazon Music"

        subcategory = heading_container.locator(f".//a[normalize-space()='{required_subcategory}']")

        expect(subcategory).to_be_visible()

        subcategory.click()

        print(f"\nPASS: '{required_subcategory}' selected.")

        browser.close()