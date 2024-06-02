from replit import clear 
from Auction_logo import logo

print(logo)

bids = {}


bidder = False

def find_highest_bidder(bidder_records):
    highest_bid  = 0
    winner = ""
    for bid in bidder_records:
        bid_amount = bidder_records[bid]
        if bid_amount > highest_bid:
            highest_bid  = bid_amount
            winner = bid
    print(f"The winner is {winner} with the bid of ${highest_bid} ")   
         
while not bidder:
    name_of_bidder = input("Please enter your name: ")
    amount = float(input("please enter the amount you would like to bid: "))
    bids[name_of_bidder] = amount
    another_bidder = input("Do you have any other bidder? Type 'yes' or 'no'.  ")
    if another_bidder == "no":
        bidder = True
        find_highest_bidder(bids)
    elif another_bidder == "yes":
        clear()    