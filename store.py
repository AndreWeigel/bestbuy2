from typing import List
from products import Product


class Store:
    """A class representing a store containing products."""

    def __init__(self, inventory: List[Product]):
        """Initialize the store with an inventory of products."""
        self.inventory = inventory

    def add_product(self, product: Product):
        """Adds a new product to the store inventory."""
        self.inventory.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store inventory."""
        if product in self.inventory:
            self.inventory.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store inventory."""
        return sum(product.get_quantity() for product in self.inventory)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store inventory."""
        return [product for product in self.inventory if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """Processes an order consisting of multiple products and quantities."""
        total_cost = 0

        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)

        return total_cost


# Test
if __name__ == "__main__":
    inventory_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(inventory_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())  # Total quantity in store

    # Process an order and print the total price
    total_price = best_buy.order([(active_products[0], 5), (active_products[1], 2)])
    print(f"Order cost: {total_price} dollars.")
