# A program that automatically prints the solution to the FizzBuzz game.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by 3 and 5, print "FizzBuzz".

for number in range(1, 101):
    if number % 3 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
