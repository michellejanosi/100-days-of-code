# A program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# A leap year is on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

year = int(input("What year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           return True
        else: 
           return False
    else: 
           return True
else:
  print(f"{year} is not a leap year.")

