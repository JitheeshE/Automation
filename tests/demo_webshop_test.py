# load the .env file

from utils.config import BASE_URL, USERNAME, PASSWORD

from dotenv import load_dotenv
load_dotenv()
import os

def test_navigate(page):
    page.goto(os.getenv("BASE_URL"))
    print(page.url)
    print(page.title())
    page.reload()
    page.goto(os.getenv("BASE_URL"))
    print(page.url)
    page.go_back()
    page.go_forward()