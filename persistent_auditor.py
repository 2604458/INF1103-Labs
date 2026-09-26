import os

def load_inventory():
    #Check if file exists first or use try-except 
    if not os.path.exists('inventory.txt'):
        return 0, []  # If file doesn't exist, start with 0 inventory

    with open('inventory.txt', 'r') as file:
        lines = file.readlines()

        #If file is empty, return defaults
        if not lines:
            return 0, []

        #First line is the total inventory
        total = int(lines[0].strip())

        #Second line is the history (if it exists)
        transaction_history = []
        if len(lines) > 1 and lines[1].strip():
            #Convert the comma separated string of numbers into a list of integers
            raw_history = lines[1].strip().split(',')
            for item in raw_history:
                if item:
                    transaction_history.append(int(item))

        return total, transaction_history

def save_inventory(total, transaction_history):
    #save the total on line 1 and the history separated by commas on line 2
    with open('inventory.txt', 'w') as file:
        file.write(str(total) + '\n')

        #Convert list of integers to a comma-separated string
        transaction_history_str = ','.join(str(x) for x in transaction_history)
        file.write(transaction_history_str + '\n')
       
def get_valid_input():
    #Handle the prompt and input validation for stock quantity
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        return 'quit'

    if not user_input.isdigit():
        print("Error:Invalid input. Please enter a valid stock quantity.")
        return None

    stock_quantity = int(user_input)
    if stock_quantity < 0:
        print("Error: Stock quantity cannot be negative.")
        return None

    return stock_quantity

def process_delivery(current_total, new_value):
    #To calculate the new total inventory and returns it
    return current_total + new_value

def calculate_tax(amount):
    #To calculate the 10% tax for a specific delivery amount
    return amount * 0.1 

def generate_report(total_units, failed_attempts, transaction_history):
    #Dedicated function to print the final summary report.
    print("\n--- Final Audit Report ---")
    print(f"Total inventory: {total_units} units")
    print(f"Transaction history: {transaction_history}")
    print(f"Invalid inputs: {failed_attempts}")

#Initialise inventory to zero 
def main():
    inventory, transaction_history = load_inventory()
    invalid_input = 0

    print (f"Loaded initial inventory: {inventory} units")

    while True:
        result = get_valid_input()

        if result == 'quit':
            break

        if result is None:
            invalid_input += 1
            continue

        #Process valid delivery
        inventory = process_delivery(inventory, result)

        #History tracking: Append valid transaction amount to the list
        transaction_history.append(result)

        tax = calculate_tax(result)
        print(f"Tax for this delivery: {tax:.2f}")

        #Overstock alert if the inventory exceeds 500 units
        if inventory > 500:
            print("Warning: Overstock alert! Inventory exceeds 500 units.")
            break

    #Write-back: Save the final total and the transaction history to the file when exiting
    save_inventory(inventory, transaction_history)
    print("Inventory and transaction history saved to 'inventory.txt'.")

    #Generate final report
    generate_report(inventory, invalid_input, transaction_history)   

if __name__ == "__main__":
    main()