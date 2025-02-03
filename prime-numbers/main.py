#
# Name Wolfgang Meyer
# Date 2-3-25
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
def is_prime(number):
    """Returns True if the number is prime, otherwise False."""
    
    # A prime number must be greater than or equal to 2
    if number < 2:
        return False
    
    # Loop through possible divisors from 2 up to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):  
        if number % i == 0:  # If divisible by any number in this range, it's not prime
            return False
    
    return True  # If no divisors were found, it's prime


def main():
    """Prompts the user to enter a number and checks if it's prime."""
    
    try:
        # Get user input
        num = int(input("Enter an integer: "))
        
        # Check if the number is prime using is_prime function
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    
    except ValueError:  
        # Handle cases where the input is not a valid integer
        print("Invalid input! Please enter an integer.")

# Run the program only if it's executed directly (not imported as a module)
if __name__ == "__main__":
    main()
