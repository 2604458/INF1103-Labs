# Lab 8 - Section 4.3: Composition test (Order <>-- OrderLine)
from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from order import Order

supplier = Supplier("S001", "TechCorp", "sales@techcorp.com")
laptop = PhysicalProduct("P001", "Laptop", 1000.00, 15, 2.5, supplier)
mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2, supplier)
antivirus = DigitalProduct("P003", "Antivirus", 45.00, 25, 350.0, supplier)

# Order creates its own OrderLines via add_order_line()
order_1 = Order("O001")
order_1.add_order_line(laptop, 1)
order_1.add_order_line(mouse, 2)
order_1.add_order_line(antivirus, 3)
order_1.display_order()  # expected total: 1000 + 51 + 135 = 1186.00

# Predict first: same Product in two different Orders
order_2 = Order("O002")
order_2.add_order_line(laptop, 2)
order_2.display_order()

line_1 = order_1.order_lines[0]
line_2 = order_2.order_lines[0]
print("\nSame Product object in both orders?", line_1.product is line_2.product)  # True
print("Same OrderLine object in both orders?", line_1 is line_2)                  # False
print(f"id(product)    = {id(line_1.product)} / {id(line_2.product)}")
print(f"id(order line) = {id(line_1)} / {id(line_2)}")
print("=> 1 Product object, 2 separate OrderLine objects (each Order made its own).")

# Remove an order line through the Order (not directly)
print("\nRemoving the Mouse line from O001 via remove_order_line()...")
order_1.remove_order_line("P002")
order_1.display_order()  # expected total: 1135.00

# order_lines returns a copy, so outside code can't change the Order's lines
order_1.order_lines.clear()
print("Lines still in O001 after clearing the returned copy:", len(order_1.order_lines))

# Removing the Order removes its lines, but the Product still exists
del order_1
print("After deleting O001, the Laptop product still exists:", laptop)
