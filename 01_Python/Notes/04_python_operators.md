# Day 3 - Python Operators

## What are Operators?

Operators are special symbols used to perform operations on variables and values.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```
15
```

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus (Remainder) | a % b |
| ** | Exponent (Power) | a ** b |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 2. Comparison (Relational) Operators

Comparison operators compare two values and return either **True** or **False**.

| Operator | Description |
|----------|-------------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

---

# Difference Between = and ==

`=` → Assignment Operator

```python
x = 10
```

`==` → Comparison Operator

```python
x == 10
```

---

# 3. Assignment Operators

Assignment operators update the value of a variable.

| Operator | Equivalent To |
|----------|---------------|
| = | x = 10 |
| += | x = x + value |
| -= | x = x - value |
| *= | x = x * value |
| /= | x = x / value |
| //= | x = x // value |
| %= | x = x % value |
| **= | x = x ** value |

Example:

```python
salary = 25000

salary += 5000
salary -= 2000
salary *= 2
salary /= 3
salary //= 4
salary %= 4
salary **= 2
```

---

# Assignments Completed

- Assignment 01 – Comparison Operators
- Assignment 02 – Assignment Operators

---

# Files Created

```
Day-03/
└── Operators/
    ├── 01_arithmetic_operators.py
    ├── 02_comparison_operators.py
    └── 03_assignment_operators.py
```

Assignments:

```
01_Python/
└── Assignments/
    ├── assignment_01.py
    └── assignment_02.py
```

---

# Key Points

- Operators perform operations on values and variables.
- Arithmetic operators are used for calculations.
- Comparison operators always return `True` or `False`.
- `=` assigns a value, while `==` compares values.
- Assignment operators provide a shorter way to update variables.

---

# Next Topic

- Logical Operators (`and`, `or`, `not`)
- Identity Operators (`is`, `is not`)
- Membership Operators (`in`, `not in`)
- Bitwise Operators