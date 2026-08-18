from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class AmazonScraper:

    def extract_products(self, page: Page):

        products = []

        cards = page.locator(
            "div[data-component-type='s-search-result']"
        )

        try:
            cards.first.wait_for(
                state="attached",
                timeout=30000
            )
        except PlaywrightTimeoutError:
            return products

        # Give Amazon a moment to finish rendering
        page.wait_for_timeout(2000)

        try:
            count = min(cards.count(), 5)
        except Exception:
            return products

        for i in range(count):

            try:
                card = cards.nth(i)

                name = "N/A"
                price = "N/A"
                rating = "No Rating"

                try:
                    name = card.locator(
                        "h2 span"
                    ).first.inner_text(timeout=5000)
                except Exception:
                    pass

                try:
                    price = card.locator(
                        ".a-price-whole"
                    ).first.inner_text(timeout=5000)
                except Exception:
                    pass

                try:
                    rating = card.locator(
                        ".a-icon-alt"
                    ).first.inner_text(timeout=5000)
                except Exception:
                    pass

                products.append({
                    "name": name,
                    "price": price,
                    "rating": rating
                })

            except Exception:
                continue

        return products