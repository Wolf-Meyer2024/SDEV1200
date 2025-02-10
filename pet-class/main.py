#
# Name Wolfgang Meyer
# Date 2-10-25
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import pet  # Import the Pet class from pet.py

def main():
    """Main function to interact with the user and create a Pet object."""
    
    # Create a Pet object
    my_pet = pet.Pet()
    
    # Get user input
    name = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter your pet's age: "))  # Convert input to an integer
    
    # Store the values in the object using setter methods
    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)
    
    # Display the pet's details using getter methods
    print("\nPet Information:")
    print("Name:", my_pet.get_name())
    print("Animal Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
