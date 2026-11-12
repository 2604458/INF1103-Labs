from product import Product

class OrderLine: 
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product 
        self.__quantity: int = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        #price * quantity for this line
        return self.__product.price * self.__quantity

    def display_information(self) -> None:
        print(f"{self.__product.name} x {self.__quantity}"
              f"@ ${self.__product.price: .2f} = ${self.calculate_subtotal(): .2f}")

class Order:
    # A customer order made up of OrderLines (composition).

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    @property
    def order_id(self) -> str:
        return self.__order_id

    @property
    def order_lines(self) -> list[OrderLine]:
        # return a copy so outside code can't add/remove lines directly
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        # The Order CREATES the OrderLine itself - this is what makes it composition.
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        # Remove the line for this product. Returns False if no such line.
        for line in self.__order_lines:
            if line.product.product_id == product_id:
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        # Ask each OrderLine for its subtotal and add them up
        return sum(line.calculate_subtotal() for line in self.__order_lines)

    def display_order(self) -> None:
        print(f"\nOrder {self.__order_id}")
        print("-" * 40)
        for line in self.__order_lines:
            line.display_information()
        print("-" * 40)
        print(f"Total: ${self.calculate_total():.2f}")
