import random

# Define card values and suits
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards
# deck = [(value, suit) for value in card_values for suit in card_suits]  # Moved inside function

# Function to calculate card value
def calculate_score(hand):
    score = 0
    aces = 0
    for card, _ in hand:
        if card in ['Jack', 'Queen', 'King']:
            score += 10
        elif card == 'Ace':
            score += 11
            aces += 1
        else:
            score += int(card)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# Function to display cards
def display_hand(name, hand):
    print(f"{name}'s Hand: {hand}, Score: {calculate_score(hand)}")

# Main game logic
def blackjack():
    deck = [(value, suit) for value in card_values for suit in card_suits]
    random.shuffle(deck)

    # Initial hands for player and dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player's turn
    while True:
        display_hand("Player", player_hand)
        if calculate_score(player_hand) > 21:
            print("Player busts! Dealer wins.")
            return "dealer"

        choice = input("Do you want to [hit] or [stand]? ").lower()
        if choice == "hit":
            player_hand.append(deck.pop())
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please choose again.")

    # Dealer's turn
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    display_hand("Dealer", dealer_hand)

    # Determine the winner
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21:
        print("Dealer busts! Player wins.")
        return "player"
    elif player_score > dealer_score:
        print("Player wins!")
        return "player"
    elif player_score < dealer_score:
        print("Dealer wins!")
        return "dealer"
    else:
        print("It's a tie!")
        return "tie"

# Run the game
if __name__ == "__main__":
    while True:
        player_wins = 0
        dealer_wins = 0
        ties = 0
        for round_num in range(1, 4):
            print(f"\nRound {round_num}")
            result = blackjack()
            if result == "player":
                player_wins += 1
            elif result == "dealer":
                dealer_wins += 1
            elif result == "tie":
                ties += 1
        print(f"\nGame Over! Player wins: {player_wins}, Dealer wins: {dealer_wins}, Ties: {ties}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break


        