"""
this is game of dice rolling.
you will play against computer will roll.
The winner gets point.
"""
import random 

def get_nuber(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("please enter a valid number")

def roll_dice() -> int:
    """
    will return a random number 
    """
    min_num = get_nuber("enter the minimum number for the dice: ")
    max_num = get_nuber("enter the maximum number for the dice: ")
    randum = random.randint(min_num, max_num) 
    return randum

def play_game():
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        input("press enter to roll the dice")
        player_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"player rolled: {player_roll}")
        print(f"computer rolled: {computer_roll}")  

        if player_roll > computer_roll:
            print("player wins")
            player_score += 1
        elif player_roll < computer_roll:
            print("computer wins")
            computer_score += 1 
        else:
            print("it's a tie") 

        print(f"Score: Player {player_score}, Computer {computer_score}")
        print()

    if player_score == 3:
        print("Player wins the game!")
    else:
        print("Computer wins the game!")

# main loop 
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
	