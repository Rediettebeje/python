print("welcome to the tip calculator")
total_bill = int(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10 12 15"))
tip_percentage = float(tip/100)
bill_percent = float(total_bill * tip_percentage)
people = int(input("how many people to split the bill? "))
each_people = round(float((bill_percent + total_bill)/people), 2)
# f-strings to insert a variable or an expression into a string.
print(f"each person should pay:{each_people } ")
