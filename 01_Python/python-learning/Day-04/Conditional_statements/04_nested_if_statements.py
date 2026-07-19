# Driving license

age =int(input("Enter your age: "))
has_license = input("Do you have a license?(yes/no): ").lower()

if age >= 18:
    if has_license == "yes":
        print("You can drive.")
    else:
        print("you need a driving license.")
else:
    print("You are too young to drive.")

# ATM withdrawal

balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount > 0:
        print("Transaction successful")
    else:
        print("Invalid amount")
else:
    print("Insufficient balance")


# Login system

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("wrong password")
else:
    print("Invalid username")


# 📝 Practice Questions
# Write these 4 programs:
# 1. College Admission
# Ask age.
# If age ≥ 17:
# Ask for percentage.
# If percentage ≥ 60 → "Admission Granted"
# Else → "Insufficient Percentage"
# Else → "Not Eligible by Age"

age = int(input('Enter your age: '))
percentage = float(input("Enter your percentage: "))

if age >= 17:
    if percentage >= 60:
        print("Admission granted")
    else:
        print("Insufficient percentage")
else:
    print("Not eligible by age ")


# 2. Online Shopping
# Ask if the user is a Prime Member (yes/no).
# If yes:
# Ask cart amount.
# If amount ≥ 500 → "Free Delivery"
# Else → "Delivery Charge Applies"
# Else:
# "Prime Membership Required"

prime_member = input("Do you have a prime membership?(yes/no): ").lower()
amount = int(input("Enter the amount: "))

if prime_member == 'yes':
    if amount >= 500:
            print("Free delivery")
    else:
        print("Delivery charge applies")
else:
    print("Prime membership required")

# 3. Exam Eligibility
# Ask attendance percentage.
# If attendance ≥ 75:
# Ask exam fee status (paid/not paid).
# If paid → "Eligible for Exam"
# Else → "Pay Exam Fee First"
#Else:
# "Attendance Shortage"

attendance_percentage = float(input("Enter your attendance percentage: "))
exam_fee_status = input("Do you have paid exam fees?(yes/no): ").lower()

if attendance_percentage >= 75:
    if exam_fee_status == 'yes':
        print("Eligible for exam ")
    else:
        print("Pay exam fee first ")
else:
    print("Attendance shorter")


# 4. ATM PIN Verification
# Correct PIN = 1234
# If PIN is correct:
# Ask withdrawal amount.
# If amount ≤ 10000 → "Transaction Successful"
# Else → "Daily Limit Exceeded"
# Else:
# "Incorrect PIN"

atm_pin = 1234
pin = int(input("Enter you pin: "))
amount = int(input("Enter the withdrawal amount:"))
if pin == 1234:
    if amount <= 10000:
        print("Transaction successful")
    else:
        print("Daily limit exceeded")
else:
    print("Incorrect PIN")
