import json
import os

from product import PhysicalProduct, Product, DigitalProduct
from inventory import Inventory
from supplier import Supplier 

FILENAME = "inventory.json"

#stored bu supplier id so we can look them up when loading from JSON
def create_suppliers() -> dict[str, Supplier]:
    suppliers = [
        Supplier ("S001", "TechCorp", "sales@techcorp.com"),
        Supplier ("S002", "SoftHouse", "contact@softhouse.com"),
    ]
    return {s.supplier_id: s for s in suppliers}

DEFAULT_SUPPLIER_ID = "S001" #used when old JSON data has no supplier_id

#for file handling
def create_default_inventory(suppliers: dict[str, Supplier]) -> Inventory:
    inventory = Inventory()
    inventory.add_product(PhysicalProduct("P001", "Laptop", 1000.00, 15, 2.5, suppliers["S001"]))
    inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2, suppliers["S001"]))
    inventory.add_product(DigitalProduct("P003", "Antivirus Software", 45.00, 25, 350.0, suppliers["S002"]))
    return inventory

#updated load logic to instantiate appropriate subclasses
def load_inventory(suppliers: dict[str, Supplier]) -> Inventory:
    if not os.path.exists(FILENAME):
        print(f"File '{FILENAME}' not found. Creating default inventory.")
        return create_default_inventory(suppliers)

    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)

            inventory = Inventory()
            for item in data:
                #for old JSON entries that were saved before lab 8
                supplier_id = item.get("supplier_id", DEFAULT_SUPPLIER_ID)
                supplier = suppliers.get(supplier_id, suppliers[DEFAULT_SUPPLIER_ID])
                
                product_type = item.get("type")
                if product_type == "physical":
                    prod = PhysicalProduct(
                        item["id"], item["name"], item["price"], item["stock"], item["weight"],
                        supplier
                    )
                elif product_type == "digital":
                    prod = DigitalProduct(
                        item["id"], item["name"], item["price"], item["stock"], item["download_size"],
                        supplier
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
        print(f"Error reading JSON file ({type(e).__name__}: {e}). Starting with default inventory.")
        return create_default_inventory(suppliers)

#updated save logic to include product type and additional attributes
def save_inventory(inventory: Inventory) -> None:
    data = []
    for p in inventory.get_products():
        item_dict = {
            "id": p.product_id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock,
            "supplier_id": p.supplier.supplier_id

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

#let the user pick an existing Supplier when adding a product
def choose_supplier(suppliers: dict[str, Supplier]) -> Supplier | None:
    print("\nAvailable suppliers:")
    for supplier in suppliers.values():
        print(f"  {supplier}")
    supplier_id = input("Enter supplier ID: ").strip().upper()
    return suppliers.get(supplier_id)

#prompt user for product type & type-specific input
def add_product_menu(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
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

    #choose supplier
    supplier = choose_supplier(suppliers)
    if supplier is None:
        print("Supplier not found. Product not added.")
        return 

    if type_choice == "1":
        try:
            weight = float(input("Enter product weight (kg): "))
            if weight < 0:
                raise ValueError
            product = PhysicalProduct(product_id, name, price, stock, weight, supplier)
        except ValueError:
            print("Invalid weight. Product not added.")
            return
    elif type_choice == "2":
        try:
            download_size = float(input("Enter download size (MB): "))
            if download_size < 0:
                raise ValueError
            product = DigitalProduct(product_id, name, price, stock, download_size, supplier)
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
    product = inventory.find_product(input("Enter Product ID: "))
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
    product = inventory.find_product(input("\nEnter Product ID: "))
    if product is None:
        print("Product not found.")
    else:
        print("\nProduct found")
        product.display_information()
        print("\nSupplier.details:")
        product.supplier.display_information()

#menu option for remove product
def remove_product_menu(inventory: Inventory) -> None:
    product_id = input("\nEnter Product ID to remove: ")
    if inventory.remove_product(product_id):
        print("Product removed from inventory.")
    else:
        print("Product not found.")

#Main

def main() -> None:
    suppliers = create_suppliers()
    inventory = load_inventory(suppliers)

    while True:
        print("\n-----------MENU-----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Inventory")
        print("6. Save Inventory")
        print("7. Exit")

        choice = input("\nEnter Option: ")

        if choice == "1":
            inventory.display_all_products()  
        elif choice == "2":
            add_product_menu(inventory, suppliers) 
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":              
            remove_product_menu(inventory)
        elif choice == "6":                  
            print("\nSaving inventory...")
            save_inventory(inventory)
        elif choice == "7":                  
            print("\nSaving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose between 1 and 7.")  


if __name__ == "__main__":
    main()
