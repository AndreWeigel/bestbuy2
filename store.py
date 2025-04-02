from typing import List
import products


class Store:
    """A class representing a store containing products."""

    def __init__(self, inventory: List[products.Product]):
        """Initialize the store with an inventory of products."""
        self.inventory = inventory

    def add_product(self, product: products.Product):
        """Adds a new product to the store inventory."""
        self.inventory.append(product)

    def remove_product(self, product: products.Product):
        """Removes a product from the store inventory."""
        if product in self.inventory:
            self.inventory.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store inventory."""
        return sum(product.get_quantity() for product in self.inventory)

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all active products in the store inventory."""
        return [product for product in self.inventory if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """Processes an order consisting of multiple products and quantities."""
        total_cost = 0

        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)

        return total_cost


