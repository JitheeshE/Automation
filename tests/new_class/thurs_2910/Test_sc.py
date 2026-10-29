import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import expect


@pytest.mark.asyncio
async def test_trace():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        try:
            page = await context.new_page()
            await page.goto("https://parabank.parasoft.com/parabank/register.htm")
            username = "1213ran1dom123"
            password = "abc@123"

            await page.locator(
                'input[name="customer.firstName"]'
            ).fill("abc")

            await page.locator(
                'input[name="customer.lastName"]'
            ).fill("a")

            await page.locator(
                'input[name="customer.address.street"]'
            ).fill("10 Test Street")

            await page.locator(
                'input[name="customer.address.city"]'
            ).fill("Bengaluru")

            await page.locator(
                'input[name="customer.address.state"]'
            ).fill("Karnataka")

            await page.locator(
                'input[name="customer.address.zipCode"]'
            ).fill("560001")

            await page.locator(
                'input[name="customer.phoneNumber"]'
            ).fill("9876543210")

            await page.locator(
                'input[name="customer.ssn"]'
            ).fill("123456789")

            await page.locator(
                'input[name="customer.username"]'
            ).fill(username)

            await page.locator(
                'input[name="customer.password"]'
            ).fill(password)

            await page.locator(
                'input[name="repeatedPassword"]'
            ).fill(password)

            # STEP 3: Submit registration
            await page.locator(
                'input[value="Register"]'
            ).click()

            # STEP 4: Validate registration result
            await expect(
                page.locator("#rightPanel")
            ).to_contain_text("Welcome")

            print("UI registration successful:", username)

           
        except Exception as e:
            print(f"error is {e}")
        finally:
            await context.tracing.stop(
                path="C:\\Users\\User\\Desktop\\Playwright_project\\tests\\new_class\\trace/trace.zip"
            )
            await context.close()
     
# POP data-driven
     
            
#3. Generating Lighthouse scores via Playwright integration 
# score :--> 0 to 100

@pytest.mark.asyncio
async def test_lighthouse_audit():
   url = "https://demowebshop.tricentis.com/"

   async with async_playwright() as p:
       browser = await p.chromium.launch(headless=True)
       page = await browser.new_page()
       await page.goto(url, wait_until="load")
       await browser.close()

   url = "https://demowebshop.tricentis.com/"
   project_dir = Path(__file__).resolve().parent
   report_path = project_dir / "lighthouse-report.json"

   result = subprocess.run(
       [
           "npx.cmd",
           "lighthouse",
           url,
           "--chrome-flags=--headless",
           "--output=json",
           f"--output-path={report_path}",
       ],
       cwd=project_dir,
       capture_output=True,
       text=True,
       timeout=180,
       shell=False,
   )


   if result.returncode != 0:
       raise RuntimeError(
           f"Lighthouse failed.\n"
           f"STDOUT:\n{result.stdout}\n"
           f"STDERR:\n{result.stderr}"
       )


   with open(report_path, encoding="utf-8") as file:
       report = json.load(file)


   for name in ("performance", "accessibility", "best-practices", "seo"):
       score = report["categories"][name]["score"]
       print(f"{name}: {score * 100:.0f}/100")
      

import json
import subprocess
from pathlib import Path

import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_lighthousejson():
    url = "https://parabank.parasoft.com/parabank/register.htm"

    # Report directory and JSON file
    report_dir = Path("C:\\Users\\User\\Desktop\\Playwright_project\\tests\\new_class\\trace\\light_house")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / "lighthouse.json"

    username = "1213ran1dom123"
    password = "abc@123"

    # STEP 1: Register user using Python Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        try:
            page = await browser.new_page()
            await page.goto(url, wait_until="domcontentloaded")

            fields = {
                'input[name="customer.firstName"]': "abc",
                'input[name="customer.lastName"]': "a",
                'input[name="customer.address.street"]': "10 Test Street",
                'input[name="customer.address.city"]': "Bengaluru",
                'input[name="customer.address.state"]': "Karnataka",
                'input[name="customer.address.zipCode"]': "560001",
                'input[name="customer.phoneNumber"]': "9876543210",
                'input[name="customer.ssn"]': "123456789",
                'input[name="customer.username"]': username,
                'input[name="customer.password"]': password,
                'input[name="repeatedPassword"]': password,
            }

            for selector, value in fields.items():
                await page.locator(selector).fill(value)

            await page.locator('input[value="Register"]').click()
            await page.wait_for_load_state("domcontentloaded")

            print("Registration submitted")
            print("Current URL:", page.url)

        finally:
            await browser.close()

    # STEP 2: Run Lighthouse audit
    try:
        res = subprocess.run(
            [
                "npx.cmd",
                "--yes",
                "lighthouse",
                url,
                "--chrome-flags=--headless",
                "--output=json",
                f"--output-path={report_file}",
            ],
            cwd=str(report_dir),
            capture_output=True,
            text=True,
            timeout=180,
            shell=False,
        )

        if res.stdout:
            print("Lighthouse output:", res.stdout)

        if res.returncode != 0:
            print("Lighthouse error:")
            print(res.stderr)
            pytest.fail("Lighthouse audit failed")

        # STEP 3: Read Lighthouse JSON report
        with report_file.open(encoding="utf-8") as f:
            json_data = json.load(f)

        # STEP 4: Print audit scores
        for name in (
            "performance",
            "accessibility",
            "best-practices",
            "seo",
        ):
            score = json_data["categories"][name]["score"]

            if score is not None:
                print(f"{name}: {score * 100:.0f} / 100")
            else:
                print(f"{name}: Score unavailable")

        print("JSON report saved to:", report_file)

    except subprocess.TimeoutExpired:
        pytest.fail("Lighthouse timed out after 180 seconds")
        

