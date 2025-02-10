#
# Name: Wolfgang Meyer
# Date: 2-10-25
# Cash Register Program using RetailItem Class
# SDEV 1200
#

# Define the RetailItem class (from the previous exercise)
class RetailItem:
    def __init__(self, description, units, price):
        """Initialize the RetailItem object with description, units in inventory, and price."""
        self.__description = description
        self.__units = units
        self.__price = price

    def set_description(self, description):
        """Set the item description."""
        self.__description = description

    def set_units(self, units):
        """Set the number of units in inventory."""
        self.__units = units

    def set_price(self, price):
        """Set the item price."""
        self.__price = price

    def get_description(self):
        """Return the item description."""
        return self.__description

    def get_units(self):
        """Return the number of units in inventory."""
        return self.__units

    def get_price(self):
        """Return the item price."""
        return self.__price


# Define the CashRegister class
class CashRegister:
    def __init__(self):
        """Initialize the CashRegister with an empty list for purchased items."""
        self.__items = []

    def purchase_item(self, item):
        """Add a RetailItem object to the list of purchased items."""
        self.__items.append(item)

    def get_total(self):
        """Return the total price of all purchased items."""
        total = sum(item.get_price() for item in self.__items)
        return total

    def show_items(self):
        """Display all purchased items."""
        print("\nItems in Cart:")
        print(f"{'Description':<20}{'Price':<10}")
        print("-" * 30)
        for item in self.__items:
            print(f"{item.get_description():<20}{item.get_price():.2f}")
        print("-" * 30)
        print(f"Total: ${self.get_total():.2f}")

    def clear(self):
        """Clear the list of purchased items."""
        self.__items = []


def main():
    """Main function to simulate a shopping experience using CashRegister and RetailItem."""
    
    # Create available retail items
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Store items in a dictionary for easy selection
    inventory = {
        "1": item1,
        "2": item2,
        "3": item3
    }

    # Create a CashRegister object
    register = CashRegister()

    # Display available items
    print("Welcome to the Retail Store!")
    while True:
        print("\nAvailable Items:")
        print("1. Jacket - $59.95")
        print("2. Designer Jeans - $34.95")
        print("3. Shirt - $24.95")
        print("4. Checkout")
        
        choice = input("Enter the number of the item to purchase (or 4 to checkout): ")

        if choice == "4":
            break
        elif choice in inventory:
            register.purchase_item(inventory[choice])
            print(f"{inventory[choice].get_description()} added to your cart.")
        else:
            print("Invalid choice, please try again.")

    # Display cart and total price
    if register.get_total() > 0:
        register.show_items()
        print("\nThank you for shopping with us!")
    else:
        print("\nNo items purchased. Thank you for visiting!")

    # Clear the cart after checkout
    register.clear()

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
