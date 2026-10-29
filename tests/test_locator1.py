

def test_table(page):
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    count_tables = page.locator("//table").count() # how many tables are pres
    print(count_tables,flush=True)
