import random

word_list = ["aardvark", "baboon", "camel"]
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#Testing code
print(f'The solution is {chosen_word}.')

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")

guess = input("Guess a letter: ").lower()


# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)