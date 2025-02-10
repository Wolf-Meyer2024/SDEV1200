#
# Name: Wolfgang Meyer
# Date: 2 - 10 - 25
# Two-Player Trivia Game
# SDEV 1200
#

import random

# Define the Question class
class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        """Initialize a Question object with a question, four possible answers, and the correct answer index."""
        self.__question = question
        self.__answers = [answer1, answer2, answer3, answer4]
        self.__correct_answer = correct_answer

    def get_question(self):
        """Return the trivia question."""
        return self.__question

    def get_answers(self):
        """Return the list of possible answers."""
        return self.__answers

    def get_correct_answer(self):
        """Return the index of the correct answer (1-4)."""
        return self.__correct_answer


def create_questions():
    """Creates and returns a list of 10 trivia Question objects."""
    return [
        Question("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3),
        Question("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2),
        Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "Jane Austen", "Ernest Hemingway", 1),
        Question("What is the largest ocean on Earth?", "Atlantic", "Indian", "Arctic", "Pacific", 4),
        Question("Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Iron", "Silver", 2),
        Question("Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3),
        Question("What is the capital of Japan?", "Seoul", "Beijing", "Bangkok", "Tokyo", 4),
        Question("Which country won the FIFA World Cup in 2018?", "Germany", "Brazil", "France", "Argentina", 3),
        Question("What is the square root of 64?", "6", "7", "8", "9", 3),
        Question("Who discovered gravity?", "Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei", 1)
    ]


def play_trivia():
    """Main function to play the trivia game between two players."""
    
    # Create 10 trivia questions
    questions = create_questions()
    
    # Shuffle the questions to randomize the order
    random.shuffle(questions)

    # Initialize player scores
    player_scores = {"Player 1": 0, "Player 2": 0}
    
    # Alternate between Player 1 and Player 2
    for i in range(len(questions)):
        current_player = "Player 1" if i % 2 == 0 else "Player 2"
        question = questions[i]

        # Display the question and possible answers
        print(f"\n{current_player}, it's your turn!")
        print(question.get_question())

        answers = question.get_answers()
        for index, answer in enumerate(answers, start=1):
            print(f"{index}. {answer}")

        # Get player's answer
        while True:
            try:
                player_choice = int(input("Enter the number of your answer (1-4): "))
                if 1 <= player_choice <= 4:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Check if the answer is correct
        if player_choice == question.get_correct_answer():
            print("Correct! 🎉 You earn a point.")
            player_scores[current_player] += 1
        else:
            print("Incorrect. 😢 No points awarded.")

    # Display final scores
    print("\nGame Over! Here are the final scores:")
    for player, score in player_scores.items():
        print(f"{player}: {score} points")

    # Determine the winner
    if player_scores["Player 1"] > player_scores["Player 2"]:
        print("\n🎉 Player 1 wins!")
    elif player_scores["Player 1"] < player_scores["Player 2"]:
        print("\n🎉 Player 2 wins!")
    else:
        print("\nIt's a tie! 🤝")

# Run the game only if this file is executed directly
if __name__ == "__main__":
    play_trivia()
