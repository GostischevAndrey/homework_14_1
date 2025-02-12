import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, "
                                                "Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def category_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, "
                    "который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def product_dict():
    return {
        "name": "Стиральная машина",
        "description": "Описание Стиральной машины",
        "price": 23450.00,
        "quantity": 5,
    }


def test_classes_category(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни")
    assert category_1.category_count == 2
    assert category_2.product_count == 4


def test_new_product(product_dict):
    product4 = Product.new_product(product_dict)
    assert product4.name == "Стиральная машина"
    assert product4.description == "Описание Стиральной машины"
    assert product4.price == 23450.00
    assert product4.quantity == 5


def test_add_product():
    product = Product("Часы", "Механические, наручные", 30000.00, 20)
    category = Category("Аксессуары", "Наручные", [])
    category.add_product(product)
    assert category._product_count == 1


def test_products_property():
    product1 = Product("Ноутбук", "Ультратонкий", 150000.00, 10)
    product2 = Product("Смартфон", "Iphone 16", 130000.00, 5)

    category = Category("Электроника", "Гаджеты и девайсы", [product1, product2])

    expected_output = ('Название продукта Ноутбук, 150000.0 руб. Остаток 10\n'
 'Название продукта Смартфон, 130000.0 руб. Остаток 5\n')
    assert category.products == expected_output
