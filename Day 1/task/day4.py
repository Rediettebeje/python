import random

# randint, will produce a random whole number between 1 and 10(inclusive)
rand_num = random.randint(1, 10)
print(rand_num)

#.random, generated a random number between 0.0(inclusive) and 1.0(not inclusive)
# 0.0 <= random.random() < 1.0
rand_num_0_to_1 = random.random()
print(rand_num_0_to_1)

#This will generate a random floating point number between 1 and 10.
# This method may or may not include the upper bound depending on the
# rounding of the floating point number. So it's best represented as:
#
# a <= random.uniform(a,b) <= b
#
# So depending on if you want the upper bound included you will choose
# whether to use random.random() or random.uniform()

random_float = random.uniform(1, 10)
print(random_float)

# coin flip program
heads_or_tails = random.randint(1, 10)
print(heads_or_tails)
if heads_or_tails >= 5:
    print("Heads")
else:
    print("Tails")
# how to pick a random name from the list of friends.

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1
# random.choice(seq)
# Return a random element from the non-empty sequence seq.
# If seq is empty, raises IndexError.
print(random.choice(friends))

# option 2
rand_friends = random.randint(0,4)
print(friends[rand_friends])
