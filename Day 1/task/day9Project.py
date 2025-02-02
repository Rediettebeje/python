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




