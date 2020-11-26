# A program that tests the compatibility between two people based on this Buzzfeed
# article: https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

# Take both people's names and check for the number of times the letters in the  word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combine_names = name1 + name2
combine_names = combine_names.lower()

t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")
true = t + r + u + e

l = combine_names.count("l")
o = combine_names.count("o")
v = combine_names.count("v")
e = combine_names.count("e")
love =  l + o + v + e 

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}. You go together like Coke and Mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}. You're alright together.")
else:
    print(f"Your score is {love_score}. Not gonna work. Sorry.")
