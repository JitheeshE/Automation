from playwright.sync_api import expect, sync_playwright

def test_demo1(page,browser_name):
    page.goto("http://192.168.10.35:5400/login")
    print(page.title())
    print("Browser name is: ", browser_name)
    expect(page).to_have_title("Flight Booking, Cheap flight tickets at Akbar Travels - Cheapest flight ticket provider | Book your holidays at cheapest rate")
    
    