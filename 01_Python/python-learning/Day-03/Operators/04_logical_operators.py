# and operator : returns true if both conditions are true

age = 23
salary = 50000

print(age > 18 and salary > 30000)  # True
print(age > 18 and salary < 30000)  # False

# or operator : returns true if at least one condition is true

age = 16

print(age >= 18 or age >=16 )  # True
print(age > 18 or age > 20)     # False

# not operator : returns true if the condition is false, and vice versa

is_logged_in = True

print(not is_logged_in)  # False
print(not False)  # True

# Practice questions
# 1. Check if a person is eligible to vote and has an aadhaar card.

age = int(input("Enter your age: "))
has_aadhaar = True
print(age >= 18 and has_aadhaar)  # True if eligible to vote and has aadhaar card

# 2. Check if a student has passed in math or science

math = 35
science = 50
print(math >= 40 or science >= 40)  # True if passed in math or science

# Use not to check if a user is not logged in 

is_logged_in = False
print(not is_logged_in)  # True if user is not logged in

# all the combinations of and & or operators

print(True and True)   # True
print(True and False)  # False  
print(False and True)  # False
print(False and False) # False

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

