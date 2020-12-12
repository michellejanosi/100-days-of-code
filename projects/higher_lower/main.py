import os, art, data, random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def choose_random():
    return random.choice(data.data)

def compare(guess, choice_a, choice_b):
    choice_a = choice_a['follower_count']
    choice_b = choice_b['follower_count']

    if choice_a > choice_b:
        return guess == 'A'
    else:
        return guess == 'B'

def play_game():
    score = 0
    continue_playing = True
    choice_a = choose_random()
    choice_b = choose_random()
    print(art.logo)

    while continue_playing:
        choice_a = choice_b
        choice_b = choose_random()

        while choice_a == choice_b:
            choice_b = choose_random()

        print(f"Compare A: {choice_a['name']}, a/an {choice_a['description']} from {choice_a['country']}")
        print(art.vs)
        print(f"Compare B: {choice_b['name']}, a/an {choice_b['description']} from {choice_b['country']}")
        guess = input("Who has a higher Instagram follower count? Type 'A' or 'B' ").upper()
        is_correct = compare(guess, choice_a, choice_b)

        clear_screen()
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_playing = False
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()