import json
import os

from product import PhysicalProduct, Product, DigitalProduct
from inventory import Inventory

FILENAME = "inventory.json"

#for file handling
def create_default_inventory() -> Inventory:
    inventory = Inventory()
    inventory.add_product(PhysicalProduct("P001", "Laptop", 1000.00, 15, 2.5))
    inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2))
    inventory.add_product(DigitalProduct("P003", "Antivirus Software", 45.00, 25, 350.0))
    return inventory

#updated load logic to instantiate appropriate subclasses
def load_inventory() -> Inventory:
    if not os.path.exists(FILENAME):
        print(f"File '{FILENAME}' not found. Creating default inventory.")
        return create_default_inventory()

    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)

            inventory = Inventory()
            for item in data:
                product_type = item.get("type")
                if product_type == "physical":
                    prod = PhysicalProduct(
                        item["id"], item["name"], item["price"], item["stock"], item["weight"]
                    )
                elif product_type == "digital":
                    prod = DigitalProduct(
                        item["id"], item["name"], item["price"], item["stock"], item["download_size"]
                    )
                else:
                    continue  # Skip unhandled or legacy data types
                
                inventory.add_product(prod)
                
            print("=" * 40)
            print("INVENTORY MANAGEMENT SYSTEM")
            print("=" * 40)
            print("\nInventory.json found.")
            print("Inventory loaded successfully.")
            return inventory
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        import traceback
        traceback.print_exc()
        print(f"Error reading JSON file ({type(e).__name__}: {e}). Starting with default inventory.")
        return create_default_inventory()

#updated save logic to include product type and additional attributes
def save_inventory(inventory: Inventory) -> None:
    data = []
    for p in inventory.get_products():
        item_dict = {
            "id": p.product_id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock,
        }
        if isinstance(p, PhysicalProduct):
            item_dict["type"] = "physical"
            item_dict["weight"] = p.weight
        elif isinstance(p, DigitalProduct):
            item_dict["type"] = "digital"
            item_dict["download_size"] = p.download_size
            
        data.append(item_dict)

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved to inventory.json successfully.")

#prompt user for product type & type-specific input
def add_product_menu(inventory: Inventory) -> None:
    print("\nAdd new product:")
    print("1. Physical Product")
    print("2. Digital Product")
    type_choice = input("Select product type (1 or 2): ")

    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        if price < 0 or stock < 0:
            raise ValueError
    except ValueError:
        print("Invalid price or stock. Product not added.")
        return

    if type_choice == "1":
        try:
            weight = float(input("Enter product weight (kg): "))
            if weight < 0:
                raise ValueError
            product = PhysicalProduct(product_id, name, price, stock, weight)
        except ValueError:
            print("Invalid weight. Product not added.")
            return
    elif type_choice == "2":
        try:
            download_size = float(input("Enter download size (MB): "))
            if download_size < 0:
                raise ValueError
            product = DigitalProduct(product_id, name, price, stock, download_size)
        except ValueError:
            print("Invalid download size. Product not added.")
            return
    else:
        print("Invalid product type choice. Product not added.")
        return

    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print("A product with that ID already exists.")


def update_stock_menu(inventory: Inventory) -> None:
    print("\nUpdate stock")
    product = inventory.search_product(input("Enter Product ID: "))
    if product is None:
        print("Product ID not found.")
        return

    print(f"Product found: \nName: {product.name}\nCurrent Stock: {product.stock}")
    try:
        product.update_stock(int(input("\nNew Stock Quantity: ")))
        print("Stock updated successfully.")
    except ValueError:
        print("Invalid quantity. Stock must be a non-negative whole number.")


def search_product_menu(inventory: Inventory) -> None:
    product = inventory.search_product(input("\nEnter Product ID: "))
    if product is None:
        print("Product not found.")
    else:
        print("\nProduct found")
        product.display_information()

#Main

def main() -> None:
    inventory = load_inventory()

    while True:
        print("\n-----------MENU-----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("\nEnter Option: ")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
