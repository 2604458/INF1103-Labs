#Initialise inventory to zero 
inventory = 0
invalid_input = 0

#Run in a continuous loop asking user to enter a stock quantity until they enter 'quit'
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        break

    #Handle invalid input (strings) using .isdigit() method
    if not user_input.isdigit():
        print("Error:Invalid input. Please enter a valid stock quantity.")
        invalid_input += 1
        continue

    #Accept stock values as integers and add them to the inventory
    stock_quantity = int(user_input)

    if stock_quantity < 0:
        print("Error: Stock quantity cannot be negative.")
        invalid_input += 1
        continue

    #Manage state, keep a running of the total inventory 
    inventory += stock_quantity

    #Trigger overstock alert if the inventory exceeds 500 units
    if inventory > 500:
        print("Warning: Overstock alert! Inventory exceeds 500 units.")
        break

#Reporting
print (f"Total inventory: {inventory} units")
print (f"Invalid inputs: {invalid_input}")