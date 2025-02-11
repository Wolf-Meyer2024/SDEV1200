#
# Name Wolfgang Meyer
# Date 2 - 10 - 25
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

# person.py

class Person:
    # Initialize the Person class with name, address, and telephone number
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    # Return a string representation of the person
    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nTelephone: {self.telephone}"

