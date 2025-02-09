import json
import os
from typing import Any, Dict, List

from src.category import Category
from src.product import Product


def load_from_json_file(file_path: str) -> list[Any]:
    """Загружает данные из файла products.json, находящегося в папке data"""
    try:
        path = os.path.join("../data/", file_path)
        with open(path, 'r', encoding='utf-8') as file:
            data: List[Any] = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def create_objects_from_json(data: List[Dict[str, Any]]) -> List[Category]:
    """Реализует подгрузку данных по категориям и товарам из файла JSON"""
    categories = []
    for category in data:
        products_data = category.get('products', [])
        products = [Product(**product) for product in products_data]

        category_data = {**category, 'products': products}
        categories.append(Category(**category_data))
    return categories


if __name__ == '__main__':  # pragma: no cover
    info = load_from_json_file("products.json")
    json_product = create_objects_from_json(info)
    print(json_product)
