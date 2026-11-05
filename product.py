from abc import ABC, abstractmethod

class Product(ABC):

#abstract base class representing a product 

    def __init__(self, product_id: str, name: str, price: float, stock: int) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

#read only accesss to the private attributes so main.py can access them but not modify them directly.
    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> None:
        #update the stock quantity of the product to a new quantity and cannot be negative.
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")  
        self.__stock = quantity

    def display_information(self) -> None:
        #print the full details of the product 
        print("-" * 40)
        print(f"id: {self.__product_id}\n"
            f"Name: {self.__name}\n"
            f"Price: ${self.__price:.2f}\n"
            f"Stock: {self.__stock}")
        print("-" * 40)

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        #abstract method forcing subclasses to define how the product is fulfilled (e.g., shipped or downloaded)
        pass

    def __str__(self) -> str:
        #oneline summary, used when listing all products
        return f"ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price:.2f}, Stock: {self.__stock}"

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float) -> None:
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    @property
    def weight(self) -> float:
        return self.__weight

    #Method overriding with super() usage
    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        print( f"Fulfilment: {self.get_fulfilment_info()}")
        print("-" * 40)

    def get_fulfilment_info(self) -> str:
        return "requires physical shipping and handling."

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float) -> None:
        #Resuse paraent constructor using super()
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    @property
    def download_size(self) -> float:
        return self.__download_size

    #Method overriding with super() usage
    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")
        print(f"Fulfilment: {self.get_fulfilment_info()}")
        print("-" * 40)

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally via download link."