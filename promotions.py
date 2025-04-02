from abc import ABC, abstractmethod

import products


class Promotion(ABC):
    """Abstract base class for promotions."""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        """Calculate the total price after applying the promotion."""
        pass


class PercentDiscount(Promotion):
    """Applies a percentage discount to the total price of the products."""
    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        if not isinstance(percentage, (int, float)) or not (0 <= percentage <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percentage = percentage

    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        """Applies the percentage discount to the total price."""
        price = product.price * quantity * (1 - self.percentage / 100)
        return price


class SecondHalfPrice(Promotion):
    """Applies a promotion where every second item is half price."""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        """Applies the second-half-price promotion."""
        discount = 0.5
        quantity_half_price = quantity // 2
        quantity_full_price = quantity - quantity_half_price

        price_half_price = quantity_half_price * product.price * discount
        price_full_price = quantity_full_price * product.price
        price = price_half_price + price_full_price

        return price


class ThirdOneFree(Promotion):
    """Applies a promotion where every third item is free."""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        """Applies the third-one-free promotion."""
        quantity_full_price = 1 - quantity // 3
        price_full_price = quantity_full_price * product.price



