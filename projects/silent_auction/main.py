from art import logo
import os

print(logo)
print("Welcome to the Secret Auction.")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

bids = {}
finished_bidding = False

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder

    return f"The winner is {winner} with a bid of ${highest_bid}."

while not finished_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")

    if other_bidders == 'no':
        finished_bidding = True
        find_highest_bidder(bids)
    elif other_bidders == 'yes':
        clear_screen()


print(find_highest_bidder(bids))
