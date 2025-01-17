print("Welcome to Python Pizza Deliveries!")
#Based on a user's order, work out their final bill.
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Small pizza (S): $15, Medium pizza (M): $20, Large pizza (L): $25
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

#Add pepperoni for small pizza (Y or N): +$2 , Add pepperoni for medium or large pizza (Y or N): +$3
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
# Add extra cheese for any size pizza (Y or N): +$1
if extra_cheese == "Y":
    price +=1
print(f"Your final bill is: ${price}." )

