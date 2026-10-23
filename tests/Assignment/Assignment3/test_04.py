import pytest
from playwright.async_api import expect
@pytest.mark.asyncio
async def test_drop(async_page):
  await async_page.goto(" https:/amazon.in")
  await async_page.get_by_role("searchbox", name="Search Amazon.in").click()
  await async_page.get_by_role("searchbox", name="Search Amazon.in").fill("bead shee")
  await async_page.get_by_role("button", name="bead sheet king size").click()
  await async_page.wait_for_timeout(3000)

  await expect(async_page.locator("#a-autoid-3").get_by_role("button", name="Add to cart")).to_be_visible()
  await async_page.locator("#a-autoid-3").get_by_role("button", name="Add to cart").click()
  await async_page.get_by_role("link", name="item in cart").click()
  await expect(async_page.get_by_role("link", name="Stoa Paris King Size Bedsheet")).to_be_visible()
  await expect(async_page.get_by_text("1", exact=True).nth(1)).to_be_visible()
  await expect(async_page.get_by_text("1,619.", exact=True)).to_be_visible()
  await async_page.get_by_role("button", name="Proceed to Buy Buy Amazon").click()