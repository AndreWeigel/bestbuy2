from abc import ABC, abstractmethod

import products


class Promotion(ABC):
    """promotion"""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self):
        pass


class PercentDiscount(Promotion):

    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        if not isinstance(percentage, (int, float)) or not (0 <= percentage <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percentage = percentage

    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        price = product.price * quantity * (1 - self.percentage / 100)
        return price


class SecondHalfPrice(Promotion):

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        discount = 0.5
        quantity_half_price = quantity // 2
        quantity_full_price = quantity - quantity_half_price

        price_half_price = quantity_half_price * product.price * discount
        price_full_price = quantity_full_price * product.price
        price = price_half_price + price_full_price

        return price


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: products.Product, quantity: int) -> float:
        quantity_full_price = 1 - quantity // 3
        price_full_price = quantity_full_price * product.price



