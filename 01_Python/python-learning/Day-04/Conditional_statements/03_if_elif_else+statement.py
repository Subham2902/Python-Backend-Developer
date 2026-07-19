num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

if num1 > num2:
    print("First number is greater")
elif num1 == num2:
    print("Both numbers are equal")
else:
    print("Second number is greater")

# PRACTICE QUESTIONS
#Write these four programs:

# 1. Grade Calculator
#90+ → Grade A
#80–89 → Grade B
#70–79 → Grade C
#40–69 → Pass
#Below 40 → Fail

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 40:
    print("Pass")
else:
    print("Fail") 


# 2. Traffic Signal

# "red" → Stop
# "yellow" → Get Ready
# "green" → Go
# Anything else → Invalid Signal

signal = input("Color of the signale(RED,GREEN,YELLOW): ").lower()

if signal == 'red':
    print("Stop")
elif signal == 'yellow':
    print("Get Ready")
elif signal == 'green':
    print('Go')
else:
    print("Invalid Signal")

# 3. Largest of Three Numbers
# Input three numbers.
# Print which one is the largest.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third  number : "))
if num1 > num2 and num1 > num3:
    print("Num1 is the largest")

elif num2 > num1 and num2 > num3:
    print("Num2 is the largest")

elif num3 > num1 and num3 > num2:
    print("Num3 is the largest")

else:
    print("All are equal")

# 4. BMI Category (Simple Version)

# BMI < 18.5 → Underweight
# BMI < 25 → Normal
# BMI < 30 → Overweight
# Otherwise → Obese

bmi = float(input("Enter your bmi: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else :
    print("Obese")