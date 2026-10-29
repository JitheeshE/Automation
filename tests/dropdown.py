@pytest.mark.asyncio
async def test_dropdown(async_page):
    async_page.goto("")
    dropdown = async_page.locator("select")
    await dropdown.click()
    await async_page.locator("option")