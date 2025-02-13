def test_classes_product(product_1):
    assert product_1.name == "55\" QLED 4K"
    assert product_1.description == "Фоновая подсветка"
    assert product_1.price == 123000.0
    assert product_1.quantity == 7


def test_price_setter(product_1):
    product_1.price = 0
    assert product_1.price == 123000.0

    product_1.price = -120000
    assert product_1.price == 123000.0


def test_valid_price_update(product_1):
    assert product_1.price == 123000.0

    product_1.price = 12000.00
    assert product_1.price == 12000.00


def test_product_str(product_2):
    assert str(product_2) == "Название продукта Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_products(product_2, product_3):
    total_value = product_2 + product_3
    expected_value = (180000.0 * 5) + (31000.0 * 14)
    assert total_value == expected_value
