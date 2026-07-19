# Day 05 - Python Conditional Statements

## 📅 Date
19 July 2026

---

# What are Conditional Statements?

Conditional statements allow a program to make decisions based on whether a condition is True or False.

Example:
- If it rains → Take an umbrella.
- If age >= 18 → Eligible to vote.

---

# 1. if Statement

### Syntax

```python
if condition:
    # code
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

# 2. if-else Statement

Executes one block if the condition is True and another if it is False.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

# 3. if-elif-else Statement

Used when there are multiple conditions.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

### Example

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

# 4. Nested if

An if statement inside another if statement.

### Syntax

```python
if condition1:
    if condition2:
        # code
```

### Example

```python
age = int(input("Enter age: "))
license = input("Do you have a license? (yes/no): ").lower()

if age >= 18:
    if license == "yes":
        print("You can drive")
    else:
        print("You need a driving license")
else:
    print("You are too young to drive")
```

---

# Operators Used

- >
- <
- >=
- <=
- ==
- !=
- and
- or
- not

---

# Important Points

- Python executes only the first matching condition in an if-elif-else block.
- Indentation is mandatory.
- Use nested if when the second condition depends on the first.
- Use `and` when checking multiple conditions together.
- Always write complete comparisons.

Correct:

```python
if num1 > num2 and num1 > num3:
```

Incorrect:

```python
if num1 > num2 and num3:
```

---

# Practice Programs

- Positive Number Check
- Voting Eligibility
- Pass/Fail
- Even/Odd
- Password Verification
- Grade Calculator
- Traffic Signal
- Largest of Three Numbers
- BMI Category
- College Admission
- Online Shopping
- Exam Eligibility
- ATM PIN Verification

---

# Key Learnings

✅ if

✅ if-else

✅ if-elif-else

✅ Nested if

✅ Logical Operators

✅ String Comparison

✅ User Input

✅ Decision Making

---

# Interview Tips

- elif means "else if".
- Nested if is used when one condition depends on another.
- Python checks conditions from top to bottom.
- After one condition becomes True, the remaining elif and else blocks are skipped.

---

# Next Topic

## Python Loops

- for loop
- range()
- while loop
- Nested loops
- break
- continue
- pass
- Pattern printing
- Practice Questions
- Assignment

---

## GitHub Commit

```bash
git add .
git commit -m "Day 5: Python Conditional Statements"
git push origin main
```

---