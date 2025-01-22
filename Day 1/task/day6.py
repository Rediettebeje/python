# A function in its simplest form is just a wrapper name for a block of
# code.It can help us save time and reduce repeated code.
import random


# Defining a new Function
def greet():
    print("Hello")
# Calling a function just means triggering the function.
# greet()

# Guess the Number Game

def guess_number():
    print("welcome to the guess the number game")
    computer_guess = random.randint(1, 101)

    user_guess = 0

    while user_guess != computer_guess:
        user_guess = int(input("guess the number\n"))
        if user_guess > computer_guess:
            print("your guess is too high")
        else:
            print("your guess is too low")

    print(f"Congratulations! You guessed it right. The number was {computer_guess}.")

guess_number()