#
# Name Wolfgang Meyer
# Date 2 - 10 - 25
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

# Define the Pet class with attributes for name, animal type, and age
class Pet:
    def __init__(self, name='', animal_type='', age=0):
        """Initialize the pet with default or provided values."""
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    def set_name(self, name):
        """Set the name of the pet."""
        self.__name = name
    
    def set_animal_type(self, animal_type):
        """Set the type of animal."""
        self.__animal_type = animal_type
    
    def set_age(self, age):
        """Set the age of the pet."""
        self.__age = age
    
    def get_name(self):
        """Return the pet's name."""
        return self.__name
    
    def get_animal_type(self):
        """Return the pet's type."""
        return self.__animal_type
    
    def get_age(self):
        """Return the pet's age."""
        return self.__age
