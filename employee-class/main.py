#
# Name Wolfgang Meyer
# Date 2-5-25
# Employee Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

class Employee:
    """A class to represent an employee with name, ID number, department, and job title."""

    def __init__(self, name, id_number, department, job_title):
        """Initialize the Employee object with attributes."""
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_info(self):
        """Displays employee information in a formatted way."""
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print("-" * 40)


def main():
    """Creates and displays Employee objects."""
    
    # Creating three Employee objects with given data
    employee1 = Employee("Luke Skywalker", 47899, "Training", "Jedi Master")
    employee2 = Employee("The Hulk", 39119, "Construction", "Demolition Worker")
    employee3 = Employee("Bullwinkle Moose", 81774, "Animation", "Cartoon Character")

    # Displaying the employee information
    print("\nEmployee Information:\n" + "=" * 40)
    employee1.display_info()
    employee2.display_info()
    employee3.display_info()


# Run the program
if __name__ == "__main__":
    main()
