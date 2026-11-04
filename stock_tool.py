class StockLookup:
    """Look up product stock counts."""

    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        """Return the first known product mentioned in the text."""
        text = text.lower()

        for product in self.stock:
            if product.lower() in text:
                return product

        return None

    def count_for(self, product):
        """Return the stock count for a product."""
        return self.stock.get(product)
