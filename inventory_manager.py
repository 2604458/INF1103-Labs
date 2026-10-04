import json
import os

def initialize_default_inventory():
    # Initialize default inventory values
    return [
        {"id": "P001", "name": "Laptop", "price": 1000.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}, 
    ]

def load_inventory():
    if not os.path.exists("inventory.json"):
        print("inventory.json not found. Starting with default inventory.")
        return initialize_default_inventory()

    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("==============================")
            print("INVENTORY MANAGEMENT SYSTEM")
            print("==============================")
            print("\nInventory.json found.")
            print("Inventory loaded successfully.")
            return inventory
    except json.JSONDecodeError:
        print("Error reading JSON file. Starting with default inventory.")
        return initialize_default_inventory()

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
        print("Inventory saved to inventory.json successfully.")

def display_all(inventory):
    print("\nCurrent Inventory:")
    print("--------------------------------")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']:.2f}, Stock: {item['stock']}")
    print("--------------------------------")

def add_product(inventory):
    #add a new product dictionary to the inventory list.
    print("\nAdd new product:")
    new_prod = {
        "id": input("Enter product ID: "),
        "name": input("Enter product name: "),
        "price": float(input("Enter product price: ")),
        "stock": int(input("Enter product stock: "))
    }
    inventory.append(new_prod)
    print("Product added successfully!")

def update_product(inventory):
    #update an existing product in the inventory list.
    print("\nUpdate stock")
    prod_id = input("Enter Product ID: ")
    for item in inventory:
        if item["id"] == prod_id:
            print(f"Product found: \nName: {item['name']}\nCurrent Stock: {item['stock']}")
            item['stock'] = int(input("\nNew Stock Quantity: "))
            print("Stock updated successfully.")
            return
    print("Product ID not found.")

def search_product(inventory):
    #search for a product in the inventory list by ID.
    prod_id = input("\nEnter Product ID: ")
    for item in inventory:
        if item["id"] == prod_id:
            print("\nProduct found")
            print("-" * 40)
            print(f"id: {item['id']}\nName: {item['name']}\nPrice: ${item['price']:.2f}\nStock: {item['stock']}")
            print("-" * 40)
            return
    print("Product not found.")

def main():
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

        if choice == '1':
            display_all(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            update_product(inventory)
        elif choice == '4':
            search_product(inventory)
        elif choice == '5':
            print("\nSaving inventory...")
            save_inventory(inventory)   
        elif choice == '6':
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