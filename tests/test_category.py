from src.product import Product


def test_classes_category(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.category_count == 2
    assert category_2.product_count == 4


def test_new_product(product_dict):
    product4 = Product.new_product(product_dict)
    assert product4.name == "Стиральная машина"
    assert product4.description == "Описание Стиральной машины"
    assert product4.price == 23450.00
    assert product4.quantity == 5


def test_add_product(product_1, category_3):
    category_3.add_product(product_1)
    assert category_3._product_count == 1


def test_products_property(product_1, product_2, category_3):
    assert (
        category_3.products == 'Название продукта 55" QLED 4K, 123000.0 руб. Остаток 7 шт.\n'
        "Название продукта Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток 5 шт.\n"
    )


def test_category_str(product_1, product_2, category_3):
    assert str(category_3) == "Название категории Электроника, количество продуктов: 12 шт."
