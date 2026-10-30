
import pytest
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from pytest_check import check

@pytest.mark.asyncio
async def test_sanity_dom_check():
    url = "https://demowebshop.tricentis.com/"
    async with (async_playwright() as p):
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        title =await page.title()
        print("title is not missing") if bool(title.strip()) else print("title is missing") #  bool("") False bool("sddd") true
        check.is_true(bool(title.strip()),"title is missing") # stop

        # alt :-->  
        missing_alt = await page.locator("img:not([alt])").count()
        print(missing_alt)
        check.equal(missing_alt,0,f"{missing_alt} num of img missing alt attribute")

        main_count = await page.locator("main").count()
        print(main_count)
        check.equal(main_count>1, f"{main_count} main land landmarks missing")

        # load axe-core js
        axe_path = Path("node_modules/axe-core/axe.min.js")
        check.is_true(
            axe_path.exists(),
            "Install axe-core using npm"
        )
        # stop the accessiblity
        if not axe_path.exists():
            return
        await page.add_script_tag(path=str(axe_path))

        # run axe-core accessablity scan
        resu = await page.evaluate(
            """
            async ()=> {
              return await axe.run(document);
            }
            """
        )
        violations = resu["violations"]

        for i in violations:
            print(
                f"Rule : {i['id']} "
                f"Impact :  {i['impact']}"
                f"Description:{i['description']}"
            )

            for j in i["nodes"]:
                print("ele affected : {j['target']}")
                print("Details: {j['failureSummary']}" )

        check.equal(
            len(violations),0,f"Accessibility violations : {len(violations)}"
        )

    await browser.close()
    
@pytest.mark.asyncio
async def test_screenshots_full_page():
    url = "https://demowebshop.tricentis.com/"
    async with (async_playwright() as p):
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        title =await page.title()
        print(title)
        # await page.screenshot(path= "D:/AI/Python_playwright/photos/demo1.png")
        ele = page.locator("input#small-searchterms")
        await ele.screenshot(path="C:/Users/User/Desktop/Playwright_project/screenshot.png")
        
from pathlib import Path
from PIL import Image, ImageChops
import pytest
from playwright.async_api import async_playwright


BASELINE = Path("screenshots/baseline.png")
ACTUAL = Path("screenshots/actual.png")
DIFF = Path("screenshots/diff.png")


@pytest.mark.asyncio
async def test_visual_regression():
   BASELINE.parent.mkdir(parents=True, exist_ok=True)
   async with async_playwright() as p:
       browser = await p.chromium.launch()
       page = await browser.new_page(
           viewport={"width": 1366, "height": 768},
           device_scale_factor=1
       )
       await page.goto(
           "https://www.amazon.in/",
           wait_until="load"
       )
       await page.screenshot(path=str(ACTUAL), full_page=True)
       await browser.close()


   assert BASELINE.exists(), (
       "Baseline missing. Capture and approve a reference image first."
   )


   with Image.open(BASELINE) as img1, Image.open(ACTUAL) as img2:
       baseline = img1.convert("RGB")
       actual = img2.convert("RGB")


       if baseline.size != actual.size:
           pytest.fail(
               f"Image dimensions differ: "
               f"{baseline.size} vs {actual.size}"
           )


       diff = ImageChops.difference(baseline, actual)
       changed_pixels = sum(
           1 for pixel in diff.getdata() if pixel != (0, 0, 0)
       )
       total_pixels = baseline.width * baseline.height
       difference_ratio = changed_pixels / total_pixels


       diff.save(DIFF)


       print(f"Changed pixels: {changed_pixels}")
       print(f"Difference ratio: {difference_ratio:.4%}")


       assert difference_ratio <= 0.01, (
           f"Visual difference exceeds 1%: "
           f"{difference_ratio:.4%}"
       )
       
async def test_create_baseline():

    BASELINE = Path("screenshots/baseline.png")

    BASELINE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        page = await browser.new_page(
            viewport={"width": 1366, "height": 768}
        )

        await page.goto(
            "https://demowebshop.tricentis.com/",
            wait_until="networkidle"
        )

        await page.wait_for_timeout(3000)

        await page.screenshot(
            path=str(BASELINE),
            full_page=True,
            animations="disabled"
        )

        print("Baseline created successfully!")
        print("Location:", BASELINE.resolve())

        await browser.close()