import pytest
from playwright.sync_api import expect


@pytest.mark.asyncio
async def test_Assertions1(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await expect(async_page).to_have_title("Demo Web Shop")
    options = async_page.locator("//li[@class='answer']")
    await expect.soft(options).to_have_count(4)
    await async_page.locator("(//li[@class='answer']) [1]").click()

