def test_count_the_link(page):
    page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
    links_locator = page.locator("//a")
    # Wait until at least one link is attached
    links_locator.first.wait_for(state="attached")
    links = links_locator.all() 
    print(len(links)) # how many links are present in the page
    print(type(links))
    for i in links:
        print(i.text_content(),flush=True) # text of the link
    print("*" * 50)
    for i in links:
        print(i.get_attribute("href"),flush=True) # href of the link
        