from playwright.sync_api import sync_playwright
from services.scraper import AmazonScraper


class BrowserService:

    def search_amazon(self, product):

        scraper = AmazonScraper()

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto("https://www.amazon.in")

            page.fill(
                "#twotabsearchtextbox",
                product
            )

            page.keyboard.press("Enter")

            page.wait_for_timeout(5000)

            products = scraper.extract_products(page)

            browser.close()

            return products