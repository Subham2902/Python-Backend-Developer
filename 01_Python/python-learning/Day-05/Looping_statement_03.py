### NESTED LOOPS - A loop inside another loops

# Example :- 1

for i in range(3):
    for j in range(3):
        print(i, j)

# Example :- 2

for i in range(1, 4):
    for j in range(1, 4):
        print(f"Row {i}, Column {j}")

### PRACTICE QUESTION

# 1. 
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 2.

for i in range(3):
    print("*")

# 3. 

for i in range(3):
    for j in range(3):
        print("*", end =" ")
    print()

    