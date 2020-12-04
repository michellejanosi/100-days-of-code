from art import logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def bidding():
    def highest_bid(bids):
        max = 0
        for bid in bids:
            if bids[bid] > max:
                max = bids[bid]

        return bid, bid[max]

    bids = {}

    name = input("What is your name?: ")
    bid = input(int("What is your bid? "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    bids.append()

    if other_bidders == 'yes':
        cls()
        bidding()
    else:
        highest_bid(bids)
        print(f"The winner is")

print(logo)
print("Welcome to the Secret Auction.")
bidding()
