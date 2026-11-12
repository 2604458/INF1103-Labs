from supplier import Supplier
from product import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechSource", "sales@techsource.com")

# 1. Create the product BEFORE any inventory exists
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5, supplier)
print("Product created on its own:")
laptop.display_information()

# 2. Add it to Inventory A
inventory_a = Inventory()
inventory_b = Inventory()
inventory_a.add_product(laptop)
print("In A?", inventory_a.find_product("P001") is not None)   # True

# 3. Remove it from A, then check the product still works
inventory_a.remove_product("P001")
print("In A after removal?", inventory_a.find_product("P001") is not None)  # False
print("Product still usable after removal:")
laptop.display_information()      # still works
laptop.update_stock(8)
print("Stock updated to:", laptop.stock)

# 4. Add the SAME object to Inventory B
inventory_b.add_product(laptop)
found = inventory_b.find_product("P001")
print("In B?", found is not None)                 # True
print("Same object as before?", found is laptop)  # True: B holds the same object, not a copy

# 5. Empty Inventory B: the product still exists
inventory_b.remove_product("P001")
print("B empty:", inventory_b.get_products() == [])
print("Product still exists:", laptop)
