def test_locators_get_by_role(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link",name="Log in").click()
    page.get_by_role("textbox",name="Email").fill("abc@gmail.com")
    page.get_by_role("textbox",name="password").fill("abc123")
    page.get_by_role("button",name="Log in").click()