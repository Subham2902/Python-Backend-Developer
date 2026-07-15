# Day 2 - Data Types & Type Conversion

## 📌 What is a Data Type?

A **data type** defines the type of value stored in a variable.

### Built-in Data Types

| Data Type | Example |
|-----------|---------|
| `int` | `10` |
| `float` | `10.5` |
| `str` | `"Subham"` |
| `bool` | `True`, `False` |
| `complex` | `2 + 3j` |

### Check Data Type

```python
a = 10
print(type(a))
```

Output:

```
<class 'int'>
```

---

# Type Conversion

Type conversion means converting one data type into another.

## Types of Type Conversion

### 1. Implicit Type Conversion

- Done automatically by Python.
- No user intervention is required.

Example:

```python
a = 10
b = 2.5

print(a + b)
```

Output:

```
12.5
```

---

### 2. Explicit Type Conversion

- Done manually using conversion functions.

Example:

```python
a = "25"
print(int(a))
```

---

# Type Conversion Functions

```python
int()
float()
str()
bool()
complex()
```

---

# Examples

### String to Integer

```python
a = "25"
print(int(a))
```

### Integer to Float

```python
a = 12
print(float(a))
```

### Float to Integer

```python
a = 9.8
print(int(a))
```

### Integer to String

```python
a = 100
print(str(a))
```

### Integer to Boolean

```python
print(bool(1))
print(bool(0))
```

---

# Boolean Conversion

## Values that become `False`

```python
bool(0)
bool("")
bool([])
bool(())
bool({})
bool(None)
```

## Values that become `True`

```python
bool(1)
bool(-5)
bool("Hello")
bool([1, 2])
bool(3.14)
```

---

# Why is `0` False?

Python treats `0` as the absence of a numeric value.

- `0` → `False`
- Any non-zero number → `True`

Example:

```python
print(bool(0))
print(bool(10))
print(bool(-2))
```

Output:

```
False
True
True
```

---

# Important Rules

```python
int("10")      # ✅
float("10.5")  # ✅
str(100)       # ✅
int(9.8)       # 9
int("abc")     # ❌ ValueError
```

---

# User Input with Type Conversion

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

---

# Key Points

- Every value has a data type.
- `type()` returns the data type of a variable.
- `input()` always returns a string.
- Use `int()`, `float()`, `str()`, `bool()`, and `complex()` for explicit type conversion.
- Python performs implicit type conversion automatically when possible.
- `0`, empty strings, empty lists, empty tuples, empty dictionaries, and `None` evaluate to `False`.

---

# Practice Completed ✅

- Convert string to integer.
- Convert integer to string.
- Convert integer to float.
- Convert float to integer.
- Take two numbers as input and print their sum.

---