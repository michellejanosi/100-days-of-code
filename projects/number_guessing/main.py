from random import randint
from art import logo
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def check_guess(user_guess, number, number_of_guesses):
    if user_guess > number:
        print("Too high")
        return number_of_guesses - 1
    elif user_guess < number:
        print("Too low")
        return number_of_guesses - 1
    else:
        print(f"The number is {number}! You guessed correct. Congrats 🥳")

def play_game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")

    difficulty = input("Choose a difficulty, 'easy' or 'hard': ")
    number = randint(1, 100)
    user_guess = 0

    if difficulty == 'easy':
        number_of_guesses = 10
    elif difficulty == 'hard':
        number_of_guesses = 5

    while user_guess != number:
        print(f"You have {number_of_guesses} attempts to guess the number.")
        user_guess = int(input("Make a guess: "))
        number_of_guesses = check_guess(user_guess, number, number_of_guesses)

        if number_of_guesses == 0:
            print(f"The number is {number}. You ran out of attempts. You lost 😭")
            break
        elif user_guess != number:
            print("Guess again")

clear_screen()
print(logo)
play_game()
