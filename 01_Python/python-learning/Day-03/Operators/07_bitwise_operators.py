# Bitwise AND (&) operator returns 1 only if both bits are 1

a = 5
b = 3
print(a & b)

# Bitwise OR (|) operator returns 1 if at least one bit is 1

print(5|3)

# Bitwise XOR(^) operators return bits are different 

print(5 ^ 3)

#Bitwise NOT(~) operators flip all bits

print(~6)

# Left Shift (<<) operators moves bits to the left 

print (5 << 1)

# Rules : << 1 = multiply by 2
#         << 2 = multiply by 4

# Right Shift (>>) operator moves bits to the right

print(5 >> 1)

# Rules : >> 1 = divided by 2(integer division)

# Practice 

print(10 & 6)
print(10 | 6)
print(10 ^ 6)
print(~10)
print(10 << 1)
print(10 >> 1)