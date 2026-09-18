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

def generate_report(total_units, failed_attempts):
    #Dedicated function to print the final summary report.
    print("\n--- Final Audit Report ---")
    print(f"Total inventory: {total_units} units")
    print(f"Invalid inputs: {failed_attempts}")

#Initialise inventory to zero 
def main():
    inventory = 0
    invalid_input = 0

    while True:
        result = get_valid_input()

        if result == 'quit':
            break

        if result is None:
            invalid_input += 1
            continue

        #Process valid delivery
        inventory = process_delivery(inventory, result)
        tax = calculate_tax(result)
        print(f"Tax for this delivery: {tax:.2f}")

        #Overstock alert if the inventory exceeds 500 units
        if inventory > 500:
            print("Warning: Overstock alert! Inventory exceeds 500 units.")
            break
    

    #Generate final report
    generate_report(inventory, invalid_input)   

if __name__ == "__main__":
    main()