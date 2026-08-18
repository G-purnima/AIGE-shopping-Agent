from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from services.scraper import AmazonScraper


class BrowserService:

    def search_amazon(self, product):

        scraper = AmazonScraper()

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            try:
                # Open Amazon
                page.goto(
                    "https://www.amazon.in",
                    wait_until="domcontentloaded",
                    timeout=60000
                )

                # Wait for search box
                page.locator("#twotabsearchtextbox").wait_for(
                    state="visible",
                    timeout=30000
                )

                # Search product
                page.fill(
                    "#twotabsearchtextbox",
                    product
                )

                page.keyboard.press("Enter")

                # Wait for navigation to finish
                try:
                    page.wait_for_load_state(
                        "domcontentloaded",
                        timeout=30000
                    )
                except PlaywrightTimeoutError:
                    pass

                # Give Amazon a little time to render products
                page.wait_for_timeout(3000)

                # Extract products
                products = scraper.extract_products(page)

                return products

            finally:
                browser.close()