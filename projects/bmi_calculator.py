# A program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It shows the interpretation of the BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

height = float(input("What is your height(m)? "))
weight = float(input("What is your weight(kg)? "))
bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}. You are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}. You are obese.")
else:
  print(f"Your BMI is {bmi}. You are clinically obese.")