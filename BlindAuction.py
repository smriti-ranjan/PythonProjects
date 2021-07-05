import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
from art import logo

print(logo)

bids = {}
bidding_finished = False


def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of Rs.{highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: Rs."))
    bids[name] = bid
    yes_no = input("Are there any other bidders? Type 'yes' or 'no'.")
    if yes_no == 'no':
        bidding_finished = True
        highest_bidder(bids)

