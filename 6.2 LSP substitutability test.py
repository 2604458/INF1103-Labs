# Lab 8 - Section 6.2 / 6.3: Liskov Substitution Principle test
from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S002", "SoftHouse", "contact@softhouse.com")
physical = PhysicalProduct("P010", "Monitor", 300.00, 5, 4.0, supplier)
digital = DigitalProduct("P011", "Photo Editor", 80.00, 100, 900.0, supplier)

# Same function, no changes, works with both subclasses
show_product_details(physical)
show_product_details(digital)

# 6.3 Expectation set by Product: update_stock() sets stock to a non-negative value
print("\nupdate_stock() keeps the same meaning for both subclasses:")
for product in (physical, digital):
    product.update_stock(42)
    print(f"  {product.name}: stock = {product.stock}")
    try:
        product.update_stock(-1)
    except ValueError as e:
        print(f"  {product.name}: rejected -1 -> {e}")

# Both product types can be used by normal Inventory operations
inventory = Inventory()
print("\nAdd both to Inventory:", inventory.add_product(physical), inventory.add_product(digital))
print("find_product works for both:",
      inventory.find_product("P010") is physical,
      inventory.find_product("P011") is digital)
print("remove_product works for both:",
      inventory.remove_product("P010"), inventory.remove_product("P011"))
