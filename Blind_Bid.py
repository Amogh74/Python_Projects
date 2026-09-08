# TODO-1: Ask the user for input
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secret Auction Program.")
Bidding = {}
run = True
while(run):
    name = input("Enter Your Name :")
    bid = int(input("Enter Your Bid :$"))
    # TODO-2: Save data into dictionary {name: price}
    Bidding[name] = bid
    # TODO-3: Whether if new bids need to be added
    want_to_continue = input("Are there any other bidders? Type Yes or No :").lower()
    if(want_to_continue == "no"):
        run = False
    else:
        print("\n" * 30)

# TODO-4: Compare bids in dictionary

max = 0
Winner = ""
for keys in Bidding:
    if(Bidding[keys] > max):
        max = Bidding[keys]
        Winner = keys
print(f"Highest Bid was of ${max} And the Winner is {Winner}")
"""
Teacher solution:
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
        """
