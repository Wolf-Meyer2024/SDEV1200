# Ingredient Adjuster Program
# Name: Wolfgang Meyer
# Date: 1-15-2025
# Course: SDEV 1200

# Dictionary to store ingredient quantities for the original recipe (in cups)
ingredients = {"Sugar (cups)": 1.5, "Butter (cups)": 1.0, "Flour (cups)": 2.75}

# Original number of cookies the recipe makes
original_batch_size = 48

# Get user input for the number of cookies desired
while True:
    try:
        desired_cookies = int(input("How many cookies would you like to make? "))
        if desired_cookies <= 0:
            print("Please enter a positive number of cookies.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Calculate the scaling factor
scaling_factor = desired_cookies / original_batch_size

# Calculate and display the adjusted ingredient amounts
print("\nIngredient amounts needed:")
for ingredient, amount in ingredients.items():
    adjusted_amount = amount * scaling_factor
    print(f"{ingredient}: {adjusted_amount:.2f} cups")

# Friendly message
print("\nHappy baking!")
