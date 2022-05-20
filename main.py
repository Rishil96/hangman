# Project 6
# Hangman

from data import words, logo, stages
from random import choice

# greet user
print(logo)
print("Welcome to Hangman!")

# randomly select a word
chosen_word = choice(words)
# print(f"Pssst, the chosen word is {chosen_word}")
# create list to hold correct guesses
guessed_letters = ["_"] * len(chosen_word)

# game lives and art
hangman_art = stages
lives = 6

# already guessed letters
already_guessed = []
user_guess = ""
# Game loop
game_is_on = True
while game_is_on:
    # ask user to guess a letter
    while user_guess in already_guessed:
        user_guess = input("Guess a letter: ").lower()

        if user_guess in already_guessed:
            print(f"You have already guessed : {user_guess}\nTry again.")

    already_guessed.append(user_guess)

    for position in range(len(chosen_word)):
        if chosen_word[position] == user_guess:
            guessed_letters[position] = user_guess
    if user_guess not in chosen_word:
        lives -= 1
        print(hangman_art[lives])
        print(f"Remaining lives: {lives}")

    # display letters guessed
    print(" ".join(guessed_letters))

    # check if game has ended
    if "_" not in guessed_letters:
        print("You Win.")
        print(f"You guessed {chosen_word} correctly.")
        game_is_on = False
    elif lives == 0:
        print("You Lose.")
        print(f"The word was {chosen_word}")
        game_is_on = False
