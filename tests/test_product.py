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
