"""
Dice Battle Game
First to 3 points wins.
Demonstrates: import, functions, loops, if statements, try/except.
"""
import random

# Function to safely get a number from the user
def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function that plays one round
def play_round():
    input("Press Enter to roll your die...")

    player_roll = roll_die()
    computer_roll = roll_die()

    print("You rolled:", player_roll)
    print("Computer rolled:", computer_roll)

    if player_roll > computer_roll:
        print("You win this round!")
        return 1
    elif player_roll < computer_roll:
        print("Computer wins this round.")
        return -1
    else:
        print("It's a tie!")
        return 0

# Main game function
def main():
    player_score = 0
    computer_score = 0

    print(" Welcome to Dice Battle! First to 3 points wins.\n")

    while player_score < 3 and computer_score < 3:
        result = play_round()

        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

        print("Score — You:", player_score, "Computer:",
computer_score)
        print()

    if player_score == 3:
        print(" You won the game!")
    else:
        print(" The computer won the game.")

# Run the program
main()