
from playwright.sync_api import expect
def test_get_by_label(page):
    page.goto("https://demowebshop.tricentis.com/")
    register_link = page.get_by_text("Register")
    register_link.click()
    page.get_by_label("Female").nth(0).check()
    page.get_by_label("First name:").fill("jitheesh")
    page.get_by_label("Last name:").fill("E")
    page.get_by_label("Email:").fill("jitheesh.e@benzyinfotech.com")
    page.get_by_label("Password:").nth(0).fill("jithi1234")
    page.wait_for_timeout(1000)