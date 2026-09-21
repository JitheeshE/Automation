from playwright.async_api import expect, async_playwright


async def test_application():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        #user 
        end_user_context = browser.new_context()
        end_user_page = end_user_context.new_page()
        end_user_page.goto("http://192.168.10.35:5400/login")
        expect(end_user_page).to_have_title("Flight Booking, Cheap flight tickets at Akbar Travels - Cheapest flight ticket provider | Book your holidays at cheapest rate")
        
        #admin
        admin_context = browser.new_context()
        admin_page = admin_context.new_page()
        admin_page.goto("http://192.168.10.38:6004/")
        expect(admin_page).to_have_title(".:: Admin Login ::.")
        
    