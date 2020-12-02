# a function that checks whether the number passed into it is a prime number or not.

check_number = int(input(f"Check this number: "))
def prime_checker(num):
    prime = True

    if num <= 1:
        prime = False
        
    for i in range(2, num):
        if num % i == 0:
            prime = False

    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

prime_checker(check_number)