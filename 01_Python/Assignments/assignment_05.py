# Q1 Take two numbers from the user and perform: (&, |, ^)

a = int(input("Enter a number:"))
b = int(input("Enter a another number:"))

print(a & b)
print(a | b)
print(a ^ b)

# Take one number from the user and print: (~, << 1, >> 1)

c = int(input("Enter a number:"))

print(~c)
print(c << 1)
print(c >> 1)

# Q3 Use:  a = 12     b = 5
# Print the result of all six bitwise operators.
a = 12
b = 5
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(~a)
print(a << b)
print(a >> b)

# Q4 Find the output without running the code:

print(8 & 4)    # 0
print(8 | 4)    # 12
print(8 ^ 4)    # 12

#Q5. (Challenge) Use:   a = 7     b = 2
# Print all six bitwise operations and write a comment beside each explaining what happened.

a = 7
b = 2

print(a & b)     # AND: Both bits must be 1 → Output: 2
print(a | b)     # OR: At least one bit must be 1 → Output: 7
print(a ^ b)     # XOR: Bits must be different → Output: 5
print(~a)        # NOT: Flips all bits of a → Output: -8
print(a << 1)    # Left Shift: Shifts bits left by 1 → Output: 14
print(a >> 1)    # Right Shift: Shifts bits right by 1 → Output: 3