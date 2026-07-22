### Break - immediately exits the loop

for i in range(1, 11):
    if i == 6:
        break
    print(i)

### Continue - skips the current iteration and moves to the next one

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

### Pass - used as a placeholder when python expects a statement

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

### PRACTICE QUESTIONS 

# 1. Print numbers from 1 to 20, but stop at 12 using break.

for i in range(1, 20):
    if i == 13:
        break
    print(i)

# 2. Print numbers from 1 to 20, but skip 8 using continue.

for i in range(1, 20):
    if i == 8:
        continue
    print(i)

# 3. question on pass

for i in range(1, 6):
    if i == 4:
        pass
    print(i)