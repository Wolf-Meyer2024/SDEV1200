#
# Name: Wolfgang Meyer
# Date: 2 - 10 - 25
# Employee & ProductionWorker Class Program
# SDEV 1200
#

# Define the Employee class
class Employee:
    def __init__(self, name, employee_number):
        """Initialize the Employee with name and employee number."""
        self.__name = name
        self.__employee_number = employee_number

    # Mutator (setter) methods
    def set_name(self, name):
        """Set the employee's name."""
        self.__name = name

    def set_employee_number(self, employee_number):
        """Set the employee's number."""
        self.__employee_number = employee_number

    # Accessor (getter) methods
    def get_name(self):
        """Return the employee's name."""
        return self.__name

    def get_employee_number(self):
        """Return the employee's number."""
        return self.__employee_number


# Define the ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        """Initialize the ProductionWorker with shift number and hourly pay rate."""
        super().__init__(name, employee_number)  # Call superclass constructor
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    # Mutator (setter) methods
    def set_shift_number(self, shift_number):
        """Set the shift number (1 = day, 2 = night)."""
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        """Set the hourly pay rate."""
        self.__hourly_pay_rate = hourly_pay_rate

    # Accessor (getter) methods
    def get_shift_number(self):
        """Return the shift number."""
        return self.__shift_number

    def get_hourly_pay_rate(self):
        """Return the hourly pay rate."""
        return self.__hourly_pay_rate


def main():
    """Main function to create and display a ProductionWorker object."""

    # Get user input
    name = input("Enter employee name: ")
    employee_number = input("Enter employee number: ")

    while True:
        try:
            shift_number = int(input("Enter shift number (1 for Day, 2 for Night): "))
            if shift_number in [1, 2]:
                break
            else:
                print("Invalid shift number! Please enter 1 for Day or 2 for Night.")
        except ValueError:
            print("Invalid input! Please enter a numeric value (1 or 2).")

    while True:
        try:
            hourly_pay_rate = float(input("Enter hourly pay rate: "))
            if hourly_pay_rate > 0:
                break
            else:
                print("Hourly pay rate must be a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

    # Create a ProductionWorker object
    worker = ProductionWorker(name, employee_number, shift_number, hourly_pay_rate)

    # Display employee details
    print("\nEmployee Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    print(f"Shift: {'Day' if worker.get_shift_number() == 1 else 'Night'}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()

