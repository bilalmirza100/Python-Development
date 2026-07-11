
bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > high_bid:
          high_bid = bid_amount
          winner = bidder 
    print(f"The winner is {winner} with a bid of ${high_bid}")
while not bidding_finished:
    print("Welcome to the secret auction program.")
    name = input("What is your name?")
    bid = int(input("What's your bid? $"))
    bids[name] = bid 
    many_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if many_bidders == "no":
        bidding_finished = True
        highest_bidder(bids)