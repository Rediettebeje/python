import random
word_list = ["aardvark", "baboon", "camel"]

# - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)
print(chosen_word)
# - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("guess a letter").lower()
#- Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for char in chosen_word:
    if guess == char:
        print("right")
    else:
        print("wrong")

# Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "-"
print(placeholder)

guess = input("Guess a letter: ").lower()
# Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "-"

print(display)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
