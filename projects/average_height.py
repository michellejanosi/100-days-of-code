# Calculates the average student height from a list of heights without using len() or sum() 

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# count the number of items in list
counter = 0
for number in student_heights:
    counter += 1

# sum the total of items in list
sum = 0
for height in student_heights:
    sum += height

avg_height = round(sum / counter)
print(avg_height)