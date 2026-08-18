from playwright.sync_api import sync_playwright
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
                page.goto(
                    "https://www.amazon.in",
                    wait_until="domcontentloaded",
                    timeout=60000
                )

                search_box = page.locator(
                    "#twotabsearchtextbox"
                )

                search_box.wait_for(
                    state="visible",
                    timeout=30000
                )

                search_box.fill(product)

                search_box.press("Enter")

                # Wait specifically for Amazon's search results
                page.wait_for_selector(
                    "div[data-component-type='s-search-result']",
                    timeout=30000
                )

                products = scraper.extract_products(page)

                return products

            finally:
                browser.close()