"""
A CLI-based interactive game where the player attempts to guess a 
random number within a limited number of tries. 
Implements input validation, exception handling (try/except), 
and state tracking using lists to enhance the user experience.
"""
import random

print("=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=")
print("Welcome to the Number Guessing Game!")
print("=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=\n")
print("I have selected a random number between 1 and 100. Can you guess it?")
print("You only have 5 attempts to guess the number. Good luck!\n")

guess_number = random.randint(1, 100)
attempts = 0
guesses = []

print(guess_number)  # For testing purposes, you can comment this line out in the final version.

while attempts < 5 and not guess_number in guesses:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess > 100 or guess < 1:
            print("Invalid guess! Please enter a number between 1 and 100.")
            continue

        attempts += 1
        guesses.append(guess)

        if guess == guess_number:
            print(f"Congratulations! You've guessed the number {guess_number} in {attempts} attempts.")
            print(f"Your guesses were: {guesses}")
            break
        elif guess < guess_number:
            print("Wrong guess! You guess is too low. Try again.")
            print(f"Your guesses so far: {guesses}")
        else:
            print("Wrong guess! You guess is too high. Try again.")
            print(f"Your guesses so far: {guesses}")

        if attempts >= 5:
            print(f"Game over! You've used all 5 attempts. The correct number was {guess_number}.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
