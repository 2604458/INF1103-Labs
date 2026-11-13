# Lab 8 - Section 2.2: Association test (Supplier <-> Product)
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct

supplier = Supplier("S001", "TechCorp", "sales@techcorp.com")
laptop = PhysicalProduct("P001", "Laptop", 1000.00, 15, 2.5, supplier)
antivirus = DigitalProduct("P002", "Antivirus", 45.00, 25, 350.0, supplier)

# Display the supplier information through each Product
print("Supplier info through the PhysicalProduct:")
laptop.supplier.display_information()
print("\nSupplier info through the DigitalProduct:")
antivirus.supplier.display_information()

# Supplier and Products are separate objects
print("\nBoth products refer to the SAME supplier object?",
      laptop.supplier is antivirus.supplier)   # True
print("Supplier and Product are separate objects?",
      laptop.supplier is not laptop)           # True

# Predict first: what happens after `del supplier`?
del supplier
print("\nAfter `del supplier` (only the variable name is removed):")
laptop.supplier.display_information()
antivirus.supplier.display_information()
print("Products still reach the supplier: the object lives on because "
      "the products still reference it.")
