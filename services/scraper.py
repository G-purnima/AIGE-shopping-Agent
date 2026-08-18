from playwright.sync_api import Page


class AmazonScraper:

    def extract_products(self, page: Page):

        products = []

        try:
            # Wait until the search result container appears
            page.wait_for_selector(
                "div[data-component-type='s-search-result']",
                timeout=30000
            )
        except Exception:
            return products

        try:
            cards = page.locator(
                "div[data-component-type='s-search-result']"
            ).all()
        except Exception:
            return products

        for card in cards[:5]:

            try:
                name = card.locator("h2 span").first.inner_text(
                    timeout=3000
                )
            except Exception:
                name = "N/A"

            try:
                price = card.locator(".a-price-whole").first.inner_text(
                    timeout=3000
                )
            except Exception:
                price = "N/A"

            try:
                rating = card.locator(".a-icon-alt").first.inner_text(
                    timeout=3000
                )
            except Exception:
                rating = "No Rating"

            products.append({
                "name": name,
                "price": price,
                "rating": rating
            })

        return products