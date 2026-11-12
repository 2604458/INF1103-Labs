from product import Product

class Inventory:
    #managers a collection of Product objects

    def __init__(self) -> None:
        self.__products = list[Product] = []

    def add_product(self, product: Product) -> bool:
        #Add a Product. Returns false if the ID already exists.
        if self.search_product(product.product_id) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        #remove the product with the given ID, returns flase if not found
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True
    
    def find_product(self, product_id: str) -> Product | None:
         #return the Product with the given ID, or None if not found.
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all_products(self) -> None:
        print("\nCurrent Inventory:")
        print("-" * 40)
        for product in self.__products:
            product.display_information()
        print("-" * 40)

    def get_products(self) -> list[Product]:
        #return a copy of the list of products
        return list(self.__products)

