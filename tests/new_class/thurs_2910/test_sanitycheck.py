import pytest
from pytest_check import check
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_sanity_dom_check():

    url = "https://parabank.parasoft.com/parabank/register.htm"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        try:
            # Open the webpage
            await page.goto(url, wait_until="domcontentloaded")

            print("\n========== DOM SANITY CHECK ==========\n")

            # 1. Check page title
            title = await page.title()

            print("Page Title:", title)

            check.is_true(
                bool(title.strip()),
                "Page title is missing"
            )

            print("Title Check: PASSED" if title.strip() else "Title Check: FAILED")

            # 2. Check images missing alt attributes
            print("\n--- Image Alt Attribute Check ---")

            missing_images = page.locator("img:not([alt])")
            missing_alt = await missing_images.count()

            print("Images missing alt attribute:", missing_alt)

            for i in range(missing_alt):
                image = missing_images.nth(i)

                src = await image.get_attribute("src")
                html = await image.evaluate("(el) => el.outerHTML")

                print(f"Image {i + 1} source:", src)
                print(f"Image {i + 1} HTML:", html)

            check.equal(
                missing_alt,
                0,
                f"{missing_alt} image(s) missing alt attribute"
            )

            print(
                "Image Alt Check: PASSED"
                if missing_alt == 0
                else "Image Alt Check: FAILED"
            )

            # 3. Check main landmark
            print("\n--- Main Landmark Check ---")

            main_landmarks = page.locator("main, [role='main']")
            main_count = await main_landmarks.count()

            print("Main landmarks found:", main_count)

            check.is_true(
                main_count >= 1,
                "Main landmark is missing"
            )

            print(
                "Main Landmark Check: PASSED"
                if main_count >= 1
                else "Main Landmark Check: FAILED"
            )

            # 4. Final summary
            print("\n========== SANITY CHECK SUMMARY ==========")
            print("Page Title:", title)
            print("Missing Image Alt Attributes:", missing_alt)
            print("Main Landmarks Found:", main_count)

            if title.strip() and missing_alt == 0 and main_count >= 1:
                print("Overall Result: PASSED")
            else:
                print("Overall Result: FAILED")

            print("==========================================\n")

        finally:
            await browser.close()
