# Pytest Tests
import pytest

from products import Product


# Test that a normal product can be created and has the correct attributes
def test_create_normal_product():
    product = Product("Test Product", 10.0, 5)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.quantity == 5
    assert product.is_active()


# Test that invalid product creation raises ValueError
def test_create_product_with_invalid_details():
    # empty name
    with pytest.raises(ValueError):
        Product("", 10.0, 5)
    # negative price
    with pytest.raises(ValueError):
        Product("Product", -10.0, 5)
    # negative quantity
    with pytest.raises(ValueError):
        Product("Product", 10.0, -5)


# Test that when quantity becomes 0 after purchase, product becomes inactive
def test_product_becomes_inactive_when_quantity_zero():
    product = Product("Test Product", 10.0, 1)
    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()


# Test that purchasing a product correctly deducts quantity and returns total price
def test_product_purchase_modifies_quantity_and_returns_price():
    product = Product("Test Product", 11.0, 6)
    total_price = product.buy(2)
    assert total_price == 22.0
    assert product.quantity == 4
    assert product.is_active()


# Test that buying more than available quantity raises ValueError
def test_buying_more_than_available_quantity_raises_exception():
    product = Product("Test Product", 10.0, 3)
    with pytest.raises(ValueError):
        product.buy(5)
