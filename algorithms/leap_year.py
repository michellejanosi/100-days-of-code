# A program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# A leap year is on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else: 
				return False
		else: 
			return True
	else:
		return False

# determin the number of days in a month in a given year

def days_in_month(year, month):
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	leap_year = is_leap_year(year)
	
	if leap_year and month == 2:
		return 29
	else: 
		return 28
	
	return month_days[month] - 1

print("Check how many days are in a given month.")
year = int(input("Enter a year: "))
month = int(input("What is the month: "))
days = days_in_month(year, month)
print(f"{days} days")
