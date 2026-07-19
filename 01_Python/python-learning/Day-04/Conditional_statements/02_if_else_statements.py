age = int(input('Enter age: '))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")    


marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Negative or Zero")


# PRACTICE QUESTIONS

# Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num  , "Number is even")
else:
    print(num  ,"Number is odd")


# Check whether a person is eligible to donate blood (age ≥ 18).

age = int(input("Enter your age: "))

if age >= 18:
    print("Person is eligible to donate blood")
else:
    print("Person is not eligible to donate blood")

# Check whether the entered password is "python123".

password = input("Enter the password: ")

if password == 'python123':
    print("Access Granted")
else:
    print("Access Denied")

# 💡 Mini Challenge (Interview Level):

#Write a program to compare two numbers and print:

# "First number is greater"
# "Second number is greater or equal"

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

if num1 > num2  :
    print("First number is greater ")
else:
    print("Second number is greater or equal  ")