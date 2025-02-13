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
        all_quantity = 0
        for i in self.__products:
            all_quantity += i.quantity
        return f"Название категории {self.name}, количество продуктов: {all_quantity} шт."

    def add_product(self, product: 'Product') -> None:
        self.__products.append(product)
        self._product_count += 1

    @property
    def products(self) -> str:
        list_products = ""
        for prod in self.__products:
            list_products += f"Название продукта {prod.name}, {prod.price} руб. Остаток {prod.quantity} шт.\n"
        return list_products
