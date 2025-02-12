from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        self._product_count = 0

    def __str__(self) -> str:
        return f'{self.name}, количество продуктов: {self.product_count} шт.'

    def add_product(self, product: 'Product') -> None:
        self.__products.append(product)
        self._product_count += 1

    @property
    def products(self) -> str:
        list_products = ""
        for prod in self.__products:
            list_products += f"Название продукта {prod.name}, {prod.price} руб. Остаток {prod.quantity}\n"
        return list_products
