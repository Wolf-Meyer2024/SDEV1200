#
# Name Wolfgang Meyer
# Date 2-3-25
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import random  # Import the random module to generate computer's choice

def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = {1: "rock", 2: "paper", 3: "scissors"}  
    return choices[random.randint(1, 3)]  # Get a random choice from 1 to 3

def get_user_choice():
    """Prompts the user to enter their choice and validates input."""
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    """Determines the winner based on the rules of Rock, Paper, Scissors."""
    if user == computer:
        return "tie"  # If both choices are the same, it's a tie
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"  # User wins
    else:
        return "computer"  # Computer wins

def main():
    """Main function to play the game until there is a winner."""
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get choices for both players
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()

        # Display choices
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie! Let's play again.")
        elif winner == "user":
            print("Congratulations! You win!")
            break  # Exit loop when the user wins
        else:
            print("Computer wins! Better luck next time.")
            break  # Exit loop when the computer wins

# Run the game
if __name__ == "__main__":
    main()

