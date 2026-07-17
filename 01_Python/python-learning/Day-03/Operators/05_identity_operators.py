# is operator returns true if both variables point to the same object in memory

a = [1, 2, 3]
b = a

print(a is b)  # True

# is not operator returns true if both variables point to different objects in memory

a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)  # True

# Practice questions
x = 10
y = x
print(x is y)
print(x is not y)