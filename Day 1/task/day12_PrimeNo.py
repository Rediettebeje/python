# a function called is_prime() that checks whether if the number passed into
# it is a prime number or not.  It should return True or False

# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

def is_prime(num):

    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2,num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
    # this return is outside the for loop which will only run once the loop finishes
    # and none of the numbers are divisible. Therefore it is prime.
    return True

print(is_prime(75))
print(is_prime(73))