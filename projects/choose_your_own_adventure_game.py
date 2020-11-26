print("Welcome to Treasure Island. Your mission is to find the treasure. Let's go!")

choice1 = input("You've come ashore but immediately come to a fork in the trees. Which way do you go: left or right? ").lower()

if choice1 == "left":
    choice2 = input("You make it through the dense trees and end up in front of a suspicious looking hut. Do you: go in or ignore? ").lower()
    if choice2 == "go in":
        choice3 = input("Though the hut looks suspicious, you go in and see 3 doors that might lead to the treasure. Which one do you choose: red, blue, or yellow? ").lower()
        if choice3 == "yellow":
            print("Congratulations! You found the treasure!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
        elif choice3 == "blue":
            print("There is a mysterious haze in the room. It's poison! You die! Game over.")
        else:
            print("The room is full of giant red flesh eating insects. You're overcome. You die! Game over.")
    else:
        print("You decide to ignore the suspicous hut and continue exploring but you quickly get lost and are attacked by savages who live on the island. Game over.")
else:
    print("You're attacked by savages who live on the island. Game over.")
