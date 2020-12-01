import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Testing code
print(f'The solution is {chosen_word}.')

print(logo)
# create blank spaces
display = []
for _ in range(word_length):
    display.append("_")


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed letter {guess}.")

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # check if incorrect guess
    if guess not in chosen_word:
        print(f"Sorry, letter {guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won")

    print(stages[lives])
