import pytest
from playwright.async_api import expect
@pytest.mark.asyncio
async def test_drop(async_page):
  await async_page.goto(" https:/amazon.in")

        # 1. Search product and verified the product using expect
  await async_page.get_by_role("searchbox", name="Search Amazon.in").click()
  await async_page.get_by_role("searchbox", name="Search Amazon.in").fill("shirt")
  await async_page.get_by_role("button", name="Jeanse for men").click()
  await expect(async_page.get_by_role("link", name="KOTTY Men's Straight Fit Jeans").nth(1)).to_be_visible()
  await async_page.wait_for_timeout(5000)

#select product and verified the title and price

  product=async_page.get_by_role("link", name="KOTTY Men's Straight Fit Jeans").nth(1)
  await product.click()
  await async_page.wait_for_timeout(5000)
  expect(async_page.get_by_role("heading", name="KOTTY Men's Straight Fit Jeans").locator("#productTitle")).to_be_visible()
  expect(async_page.locator("#corePrice_feature_div").get_by_text("849.", exact=True)).to_be_visible()