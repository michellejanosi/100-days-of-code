# An automatic pizza order program.
# small: $10
#  plus pepperoni: +$2  
# medium: $12
#  plus pepperoni medium or large: +$3
# large: $15
# extra cheese: +$1

print("Welcome to Python Pizza Delivers")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill += 12
else:
    bill += 15

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
