from playwright.sync_api import expect

# def test_locators_get_by_role(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     page.get_by_role("link",name="Log in").click()
#     page.get_by_role("textbox",name="Email").fill("abc@gmail.com")
#     page.get_by_role("textbox",name="password").fill("abc123")
#     page.get_by_role("button",name="Log in").click()
    
# def get_by_text(page):
#     page.goto("http://192.168.10.35:5400/login")
#     login_to_akbar_text = page.get_by_text("A Travel Agent ?")
#     expect(login_to_akbar_text).to_be_visible()
#     forgot_password_button = page.get_by_text("Forgot Password?")
#     forgot_password_button.click()
    
# page.getByLabel() to locate a form control by associated label text.
def get_by_label(page):
    page.goto("https://demowebshop.tricentis.com/")
    register_link = page.get_by_text("Register")
    register_link.click()
    page.get_by_label("First name").fill("John")
    
    
    
    
