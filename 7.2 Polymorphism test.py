# Lab 8 - Section 7.2: Polymorphism test (mixed Product types, one loop)
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechCorp", "sales@techcorp.com")
inventory = Inventory()
inventory.add_product(PhysicalProduct("P001", "Laptop", 1000.00, 15, 2.5, supplier))
inventory.add_product(DigitalProduct("P002", "Antivirus", 45.00, 25, 350.0, supplier))

# One loop, no isinstance(): each object supplies its own implementation
for product in inventory.get_products():
    product.display_information()
    print(f"get_fulfilment_info(): {product.get_fulfilment_info()}")
