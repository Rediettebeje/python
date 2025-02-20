# a function called is_prime() that checks whether if the number passed into
# it is a prime number or not.  It should return True or False

# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

def is_prime(num):

    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(is_prime(75))
print(is_prime(73))