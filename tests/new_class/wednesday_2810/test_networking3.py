import asyncio
import pytest
from playwright.async_api import async_playwrightpython -m pytest test_networking2.py -v -s
@pytest.mark.asyncio
async def test_slow_network():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        # slow
        async def slowapi(route):
            print(route.request.url)
            await asyncio.sleep(3)
            await route.continue_()
        await page.route(
            "**/api/**",slowapi
        )

        await page.goto("https://demowebshop.tricentis.com/")
        await page.wait_for_timeout(5000)
        await browser.close()