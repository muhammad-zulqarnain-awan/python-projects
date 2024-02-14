import sys
import os

def clear():
    os.system('cls')

def find_highest(bid_dict):

    name = ''
    highest = 0

    for bid in bid_dict:
        amount = bid_dict[bid]
        if amount > highest:
            highest = amount
            name = bid

    return (f"The winner is {name} with a bid of ${highest}.")
    



print("Welcome to the Secret Auction Program")
end = False
bidder_dict = {}

while end != True:

    bidder_name = input("Bidder name: ")
    bid_value = int(input("Bid: $"))

    bidder_dict[bidder_name] = bid_value

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")


    if next_bidder.lower() == 'yes':
        clear()

    elif next_bidder.lower() == 'no':
        print(find_highest(bidder_dict))
        end = True
