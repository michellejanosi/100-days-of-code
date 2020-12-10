############DEBUGGING#####################

# Describe Problem
# The problem is "You got it" does not print. It is because i never equals 20. The stop argument in the range function is not inclusive." To correct, increase stop argument in range function by 1
# def my_function():
#   for i in range(1, 20):
#     # print(i)  
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# Bug can be reproduced by changing the value of dice_num to an index that is greater than the number of indexes in dice_imgs. To fix the bug, change the range to count like a computer, "0, 5"
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Play Computer
# If an input includes a year, ex. 1994, that is not true for the statement given, nothing is printed. To fix, you can increase and decrease the range of years or just include an else statement to accomodate a year that is not included in the range given.
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# The first error when running this code is: "IndentationError: expected an indented block" which tells me line of code needs to be indented. In this case, it's line 31. The next error, "TypeError: '>' not supported between instances of 'str' and 'int'" occurs because input returns a string unless you convert it to, in this case, an integer. You can compare int not str here. The last error is not an error at all but the code does not return what you would expect, "You can drive at age {age}." These are the trickiest of bugs because there are not clues telling you what the problem is though this one is easy, an f string is needed to correct the error.
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# use print() to check the value of the inputs for pages and word_per_page. In this case, word_per_page is 0 and does not change from its initial value because line 38 is checking equality not actually assigning a value, "==" vs "="
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)

# #Use a Debugger
# at pythontutor.com
# of course the bug is indentation on line 51. This is a common error for me but one I am recognizing more often than previously
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])