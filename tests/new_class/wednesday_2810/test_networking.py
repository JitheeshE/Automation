
import asyncio
import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_slow_network():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Simulate a slow API response
        async def slowapi(route):
            print("Intercepted URL:", route.request.url)
            await asyncio.sleep(3)
            await route.continue_()

        # Intercept API requests and delay them by 3 seconds
        await page.route("**/api/**", slowapi)

        await page.goto("https://demowebshop.tricentis.com/")

        await page.wait_for_timeout(5000)

        await browser.close()
