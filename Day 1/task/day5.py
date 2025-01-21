student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

#max, min, built-in functions
maxi_score = max(student_scores)
mini_score = min(student_scores)

print(mini_score)
print(maxi_score)

# Loops allow us to tell the computer to repeat actions
# without having to write repeated code
# Loops allow us to create a rule and the computer
# can follow it to do a repeated action

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

#sum, built-in functions
total_score = sum(student_scores)
print(total_score)

# using for loop to find the sum of the list
sum = 0
for score in student_scores:
    sum += score
print(sum)


#The combination of the range() function with the Python For Loop
# allows us to run a loop for as many times as we wish. Instead of looping
# through each item in a List, we can loop through a range of numbers.

# a <= range(a, b) < b
# Where the range of numbers is inclusive of the lower bound
# but not inclusive of the upper bound

sum = 0
for numbers in range(1,101):
    sum += numbers
print(sum)