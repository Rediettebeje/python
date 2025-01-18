
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
