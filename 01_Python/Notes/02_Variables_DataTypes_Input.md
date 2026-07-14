# Day 2 - Variables, Data Types, User Input & Type Conversion

## Variables

A variable is a container used to store data.

Example:

```python
name = "Subham"
age = 23
height = 179.5
```

---

## Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| str | Text | "Python" |
| int | Whole Numbers | 25 |
| float | Decimal Numbers | 25.5 |
| bool | True or False | True |

### Examples

```python
name = "Subham"
age = 23
height = 179.5
is_student = False
```

---

## Variable Naming Rules

### Valid

```python
name
student_name
age23
_marks
```

### Invalid

```python
2name
student name
class
```

### Rules

- Use letters, numbers and underscores.
- Cannot start with a number.
- Spaces are not allowed.
- Variable names are case-sensitive.
- Do not use Python keywords.

---

## User Input

Used to take input from the user.

```python
name = input("Enter your name: ")
```

### Important

`input()` always returns a **string**.

---

## Type Conversion

Convert one data type into another.

### String → Integer

```python
age = int("23")
```

### String → Float

```python
height = float("179.5")
```

### Integer → String

```python
marks = str(95)
```

---

## Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)
```

---

## Important Concepts

Without conversion:

```python
num1 = input()
num2 = input()

print(num1 + num2)
```

Input

```
10
20
```

Output

```
1020
```

With conversion:

```python
num1 = int(input())
num2 = int(input())

print(num1 + num2)
```

Output

```
30
```

---

## Key Points

- Variables store data.
- Python has four basic data types:
  - str
  - int
  - float
  - bool
- `input()` always returns a string.
- Use `int()` and `float()` for numeric input.
- Follow proper variable naming rules.

---

## Today's Practice

- Created variables
- Learned data types
- Used input()
- Performed type conversion
- Wrote simple Python programs