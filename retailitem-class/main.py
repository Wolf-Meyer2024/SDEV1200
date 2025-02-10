#
# Name: Wolfgang Meyer
# Date: 2-10-25
# Retail Item Class Program
# SDEV 1200
#

# Define the RetailItem class with attributes for item description, units in inventory, and price
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

def main():
    """Main function to create and display RetailItem objects."""

    # Create three RetailItem objects with the given data
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Store the items in a list for easier iteration
    items = [item1, item2, item3]

    # Display the data for each retail item
    print("\nRetail Store Inventory:")
    print(f"{'Item':<10}{'Description':<20}{'Units in Inventory':<20}{'Price'}")
    print("-" * 60)

    for i, item in enumerate(items, start=1):
        print(f"Item #{i:<6}{item.get_description():<20}{item.get_units():<20}{item.get_price():.2f}")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
