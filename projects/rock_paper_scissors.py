import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Rock wins against Scissors.
# Scissors win against Paper.
# Paper wins against Rock.

player = int(input("What do you choose? Pick 0 for Rock, 1 for Paper, or 2 for Scissors. "))
choice = [0, 1, 2]
computer = random.choice(choice)

if player == 0:
    if computer == 0:
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a draw")
    elif computer == 1:
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose")
    else:
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You won")
elif player == 1:
    if computer == 0:
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win")
    elif computer == 1:
        print(paper)
        print("Computer chose:")
        print(paper)
        print("It's a draw")
    else:
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose")
else:
    if computer == 0:
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You lose")
    elif computer == 1:
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You win")
    else:
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("It's a draw")