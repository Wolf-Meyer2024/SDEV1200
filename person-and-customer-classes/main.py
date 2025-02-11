# 
# Name: Wolfgang Meyer
# Date: 2 - 10 - 25
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Import the Person class from the person module
import person

# Define the Customer class, which inherits from Person
class Customer(person.Person):
    # Initialize the Customer class with name, address, telephone, customer number, and mailing list status
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        # Call the parent (Person) class __init__ method
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list

    # Return a string representation of the customer, adding customer-specific details
    def __str__(self):
        return super().__str__() + f"\nCustomer Number: {self.customer_number}\nMailing List: {'Yes' if self.on_mailing_list else 'No'}"

# Main function
def main():
    # Local variables
    name = "John Doe"
    address = "123 Elm St"
    telephone = "555-1234"
    customer_number = "C12345"
    on_mailing_list = True

    # Create an instance of the Customer class using the data attributes
    customer1 = Customer(name, address, telephone, customer_number, on_mailing_list)

    # Display the information about the customer
    print(customer1)

# Call the main function to run the program
main()

