# Ask the user for input
name = input("What is your name?: ")
price = int(input("What is your bid?: $"))
# Save data into dictionary {name: price}
bidsData = {}
bidsData[name] = price
# print(bidsData)
#  Whether if new bids need to be added

is_there = True
while is_there:
    askUser =  input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if askUser == "yes":
        # There are several ways of clearing the output. The easiest is to simply
        # print "\n" many times so that the output scrolls down many lines.
        print( "\n" * 100)
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bidsData[name] = price
    else:
        is_there = False


print(bidsData)
# Compare bids in dictionary
max_bid = 0
for bid in bidsData:
    # print(bidsData[bid] )
    if bidsData[bid] > max_bid:
        max_bid = bidsData[bid]
print(max_bid)



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

