import random
from art import logo_blackjack

def deal_card():
    """Returns a random card from the deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cards)
    return random.choice(cards)

def calculate_score(a):
    """Calculate the score of the hand given. Returns 0 is its a blackjack"""
    if sum(a) == 21 and len(a) == 2:
        return 0

    if 11 in a and sum(a) > 21:
        a.remove(11)
        a.append(1)
    return sum(a)

def compare(a,b):
    """Compares the given inputs and gives the final output based on the conditions satisfied"""
    if a == b:
        return "Its a Draw.\n"
    elif b == 0:
        return "Dealer has a blackjack. You lose!\n"
    elif a ==0:
        return "You have a blackjack. You win!\n"
    elif a > 21:
        return "You went over. You lose!\n"
    elif b > 21:
        return "Dealer went over. You Win!\n"
    elif a > b:
        return "You win!\n"
    else:
        return "You lose!\n"

def game_start():
    """The BlackJack Game. It takes user input and gives output based on the winner"""
    print(logo)
    user_hand = []
    computer_hand = []
    game_over = False
    user_score = 0
    computer_score = 0

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not game_over:
        user_score =  calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"\n      Your Cards: {user_hand}, current score: {user_score}\n")
        print(f"        Computer's first card: [{computer_hand[0]}]\n")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'hit me' to get another card, type 'pass' to pass: \n").lower()
            if another_card == 'hit me':
                user_hand.append(deal_card())
                calculate_score(user_hand)
            else:
                game_over = True

    while calculate_score(computer_hand) < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"    Your final hand: {user_hand}, final score: {sum(user_hand)}\n")
    print(f"    Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}\n")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower() == 'y':
    print("\n" * 20)
    game_start()



