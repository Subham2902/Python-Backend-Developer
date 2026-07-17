# Q1 A user can log in only if:
# Username is "admin"
# Password is "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")

print(username == "admin" and password == "python1234")  # True if both username and password are correct

# Q2 A customer can gets free delivery if:
# Order amount is Rs. 500 or more or they are a premium member
# Print whether they gets free delivery.

order_amount = int(input("Enter your order amount: "))
premium_member = input("Are you a premium member? (yes/no): ").lower() == "yes"
is_premium = True  # Assuming the customer is a premium member

print(order_amount >= 500 or is_premium)  # True if order amount is 500 or more or they are a premium member

# Q3 A shop is closed if is_holiday is True. Use the not operator to print whether the shop is open.

is_holiday = input("Is it a holiday? (yes/no): ").lower() == "yes"
print(not is_holiday)  # True if the shop is open (not a holiday)   

# Q4 A person is eligible for a driving license if: Age is 18 or above
#  Eyesight test is passed Print the result.

age = int(input("Enter your age: "))
eyesight_test_passed = input("Have you passed the eyesight test? (yes/no): ").lower() == "yes"
print(age >= 18 and eyesight_test_passed)  # True if eligible for a driving license (age is 18 or above and eyesight test is passed)

# Q5 Create 3 variables of your choice and write 3 different logical 
# expressions using and, or, and not. Print the result of each.

has_ticket = True
temperature = 30
is_weekend = False

print(has_ticket and temperature > 25)  # True if has ticket and temperature is above 25
print(is_weekend or has_ticket)   # True if it is weekend or has ticket
print(not is_weekend)  # True if it is not a weekend