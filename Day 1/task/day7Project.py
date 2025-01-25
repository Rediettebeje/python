import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

# For each letter in the chosen_word, add a _ to placeholder
placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won.
game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            #previous guesses are added to the display String.
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
           # print statement below to give the user the correct word they were trying to guess
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
