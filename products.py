#import promotions


class Product:
    """
    Represents a product with a name, price, and quantity.
    Manages product availability and purchasing logic.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a new product with a name, price, and quantity."""

        if not isinstance(name, str) or not name:
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Product price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Product quantity must be a non-negative integer.")

        self.name = name
        self.price = price
        self._quantity = quantity
        self.active = True
        self.promotion = None

    @property
    def quantity(self) -> int:
        """Returns the current quantity of the product."""

        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        """Updates the product quantity and deactivates the product if quantity reaches zero."""

        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self._quantity = new_quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Checks whether the product is currently active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""

        self.active = False

    def show(self) -> str:
        """Displays the product's details."""

        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        print(product_info)
        return product_info

    def buy(self, purchace_quantity: int) -> float:
        """Processes the purchase of a specified quantity of the product."""

        if not isinstance(purchace_quantity, int) or purchace_quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if purchace_quantity > self._quantity:
            raise ValueError("Insufficient product quantity.")

        total_price = self.price * purchace_quantity
        self._quantity -= purchace_quantity

        if self._quantity == 0:
            self.deactivate()

        return total_price


# Subclass for non-stocked products
class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Prevents changing quantity for non-stocked items"""
        pass

    def show(self) -> str:
        """Displays the product's details."""

        product_info = (f"{self.name}, Price: {self.price}"
                        f" (Non-stocked product: quantity is unlimited)")
        print(product_info)
        return product_info

    def buy(self, purchace_quantity: int) -> float:
        """Processes the purchase of a specified quantity of the product."""
        if not isinstance(purchace_quantity, int) or purchace_quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        total_price = self.price * purchace_quantity
        return total_price


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum per order must be a positive integer.")
        self.maximum = maximum

    def buy(self, purchace_quantity: int) -> float:
        """Processes the purchase of a specified quantity of the product."""
        if not isinstance(purchace_quantity, int) or purchace_quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if purchace_quantity > self.maximum:
            raise ValueError(f"It is not possible purchase more than {self.maximum} "
                             f"units per order.")
        total_price = super().buy(purchace_quantity)
        return total_price

    def show(self) -> str:
        """Displays the product's details."""

        product_info = (f"{self.name}, Price: {self.price}, Quantity: {self._quantity}"
                        f" (Limited to {self.maximum} per order)")
        print(product_info)
        return product_info
