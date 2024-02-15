
import random
import os
import logo

def clear():
    os.system('cls')

def deal_card(cards_deck):
    return random.choice(cards_deck)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

    
def compare(user_score, comp_score):
    if user_score == comp_score:
        print("Draw")
    elif user_score == 0:
        print("You Won!\nYou have a blackjack.")
    elif comp_score == 0:
        print("Dealer Won!\nDealer has a blackjack.")
    elif user_score > 21:
        print("You went over!\nYou Lose!")
    elif comp_score > 21:
        print("Dealer went over!\nYou Won!")
    elif user_score > comp_score:
        print("You Won!")
    else:
        print("You Lose!")

    
def play_game():

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    user_cards = [deal_card(cards) for _ in range(2)]
    comp_cards = [deal_card(cards) for _ in range(2)]

    end = False

    while not end:

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards: {user_cards}\nCurrent Score: {user_score}\n")
        print(f"Dealer cards: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            end = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                user_cards.append(deal_card(cards))
            else:
                print("Thank you playing Blackjack...")
                end = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card(cards))
        comp_score = calculate_score(comp_cards)
    print(f"Your final cards: {user_cards}\nFinal Score: {user_score}\n")
    print(f"Dealer final cards: {comp_cards}\nFinal Score: {comp_score}")
    compare(user_score,comp_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(logo.logo)
    play_game()


