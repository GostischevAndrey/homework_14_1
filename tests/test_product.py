import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


def test_classes_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_price_setter():
    product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    product.price = 0
    assert product.price == 123000.0

    product.price = -120000
    assert product.price == 123000.0


def test_valid_price_update():
    product = Product("Клавиатура", "Механическая клавиатура", 10000.00, 30)
    assert product.price == 10000.00

    product.price = 12000.00
    assert product.price == 12000.00
