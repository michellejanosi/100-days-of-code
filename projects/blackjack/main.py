from art import logo
import os
import random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def check_score(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        return "You busted! You lose 😖"
    
    if user_score == dealer_score:
        return "It's a draw 🙃"
    elif dealer_score == 0:
        return "Dealer Blackjack. You lose 😭"
    elif user_score == 0:
        return "Blackjack! You win 🥳💰"
    elif user_score > 21:
        return "You busted! You lose 😖"
    elif dealer_score > 21:
        return "Dealer busted! You win 🥳💰"
    elif user_score > dealer_score:
        return "You win 🥳💰"
    else:
        return "You lose 😖"

def play_blackjack():
    print(logo)
    print("A score of '0' is equal to a 'Blackjack'")

    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, your hand equals: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            get_another_card = input("Type 'hit' to get another card, 'stand' to hold your total: ")

            if get_another_card == 'hit':
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, total: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, total: {dealer_score}")
    print(check_score(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n': ") == 'y':
    clear_screen()
    play_blackjack()
