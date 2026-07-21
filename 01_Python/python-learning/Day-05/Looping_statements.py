# ---------- LOOPS ----------

###   FOR LOOPS   ###  

for i in range(5):
    print(i)

print('------------------------------------------------------')

# range() function 

for i in range(1,6):
    print(i)

print('-------------------------------------------------------')

# Even numbers 

for i in range(2, 11, 2):
    print(i)

print('-------------------------------------------------------')

# Reverse order

for i in range(10, 0, -1):
    print(i)

print('-------------------------------------------------------')

###   WHILE LOOP   ###

i = 1
while i <= 5:
    print(i)
    i += 1


# PRACTICE QUESTION

# 1. Print numbers from 1 to 20.

for i in range(0,21):
    print(i)

# 2. Print even numbers from 1 to 50.

for i in range(2, 51, 2):
    print(i)

# 3. Print odd numbers from 1 to 50.

for i in range(1, 51, 2):
    print(i)

# 4. Print numbers from 20 to 1.

for i in range (20, 0, -1):
    print(i)

# 5. Print the multiplication table of 7.

for i in range (0, 71, 7):
    print(i)

# 6. Find the sum of numbers from 1 to 100.

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

# 7. Print the squares of numbers from 1 to 10.

for i in range(1, 11):
    print(i ** 2)

# 8. Print each character of your name using a for loop.

name = "Subham"
for char in name:
    print(char)

# 9. Print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i += 1

# 10. Print even numbers from 2 to 20 using a while loop.

num = 2
while num <= 20:
    print(num)
    num += 2
