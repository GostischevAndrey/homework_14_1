import json

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, load_from_json_file


@pytest.fixture
def load_from_json_file_return(tmpdir):
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
                           "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    file = tmpdir.join("products.json")
    file.write(json.dumps(data))
    return str(file)


def test_not_load_fromjson_file():
    assert load_from_json_file("products1.json") == []


def test_load_from_json_file(load_from_json_file_return):
    data = load_from_json_file(load_from_json_file_return)
    assert len(data) == 1
    assert data[0]["name"] == "Смартфоны"
    assert len(data[0]["products"]) == 1


def test_create_objects_from_json(load_from_json_file_return):
    data = load_from_json_file(load_from_json_file_return)
    categories = create_objects_from_json(data)
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
