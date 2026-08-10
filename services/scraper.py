from playwright.sync_api import Page


class AmazonScraper:

    def extract_products(self, page: Page):

        products = []

        cards = page.locator("div[data-component-type='s-search-result']")

        count = min(cards.count(), 5)

        for i in range(count):

            card = cards.nth(i)

            try:

                name = card.locator("h2 span").inner_text()

            except:
                name = "N/A"

            try:

                price = card.locator(".a-price-whole").first.inner_text()

            except:
                price = "N/A"

            try:

                rating = card.locator(".a-icon-alt").first.inner_text()

            except:
                rating = "No Rating"

            products.append(
                {
                    "name": name,
                    "price": price,
                    "rating": rating,
                }
            )

        return products