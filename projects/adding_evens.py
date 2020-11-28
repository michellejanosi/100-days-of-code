# Calculates the sum of all the even numbers from 1 to 100, including 1 and 100.

sum = 0
for number in range(2, 101, 2):
    sum += number

print(sum)