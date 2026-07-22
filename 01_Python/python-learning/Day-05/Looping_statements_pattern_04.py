# Print the pattern

# 1. 

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = " ")
    print()

# 2. 

print("-------------------------------------------------------------------")
for i in range(5, 0, -1):
    for j in range(i):
        print("*",end = " ")
    print()

# 3. 

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

# 4. 

for i in range (1, 6):
    for j in range(1, i + 1):
        print(i, end = " ")
    print()