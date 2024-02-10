from hangman_art import *
from hangman_words import word_list
import random

print(logo)

guessed_word = random.choice(word_list)

user_guess = ["_" for _ in range(len(guessed_word))]

end = False
lives = len(stages)

while end != True and lives >= 0:

    user_input = input("\nGuess the letter: ")
    
    if user_input in user_guess:
        print(f"\nYou have already guessed {user_input} ")

    for index in range(len(guessed_word)):
        letter = guessed_word[index]
        if letter == user_input:
            user_guess[index] = letter
    print(' '.join(user_guess))

    if "_" not in user_guess:
        end = True
        print("Hurray!\nYou won!")

    if user_input not in guessed_word:
        print(stages[lives-1])
        lives -= 1

        if lives == 0:
            print("Oh no!\nYou Lose!")
            end = True
    
    


