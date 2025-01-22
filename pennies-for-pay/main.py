#
# Name Wolfgang Meyer
# Date 1 - 22 - 2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.
def calculate_salary():
    # Ask the user for the number of days
    days = int(input("Enter the number of days: "))
    
    # Initialize variables
    total_pennies = 0
    current_salary = 1  # Salary in pennies on the first day
    
    # Display the table header
    print("\nDay\tSalary (dollars)")
    print("-------------------------")
    
    # Loop through each day to calculate salary
    for day in range(1, days + 1):
        salary_in_dollars = current_salary / 100  # Convert pennies to dollars
        print(f"{day}\t${salary_in_dollars:.2f}")
        total_pennies += current_salary  # Add the current day's salary to the total
        current_salary *= 2  # Double the salary for the next day
    
    # Display the total pay
    total_pay_dollars = total_pennies / 100  # Convert total pennies to dollars
    print(f"\nTotal pay after {days} days: ${total_pay_dollars:.2f}")

# Run the program
calculate_salary()
