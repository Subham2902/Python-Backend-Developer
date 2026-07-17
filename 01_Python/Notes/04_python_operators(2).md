# Day 3 (Part 2) - Logical, Identity, Membership & Bitwise Operators

---

# Logical Operators

Logical operators are used to combine multiple conditions.

## Types

- `and`
- `or`
- `not`

---

## AND (`and`)

Returns `True` only if **both conditions are True**.

### Example

```python
age = 23
salary = 50000

print(age >= 18 and salary >= 30000)
```

**Output**

```python
True
```

---

## OR (`or`)

Returns `True` if **at least one condition is True**.

### Example

```python
age = 16

print(age >= 18 or age >= 16)
```

**Output**

```python
True
```

---

## NOT (`not`)

Reverses the Boolean value.

### Example

```python
is_logged_in = True

print(not is_logged_in)
```

**Output**

```python
False
```

---

## Truth Table

| A | B | A and B | A or B |
|---|---|----------|---------|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

---

## Uses

- Login systems
- Eligibility checking
- Input validation
- Multiple condition checking

---

# Identity Operators

Identity operators check whether two variables refer to the **same object in memory**.

## Types

- `is`
- `is not`

---

## `is`

Returns `True` if both variables refer to the same object.

```python
a = [1, 2, 3]
b = a

print(a is b)
```

**Output**

```python
True
```

---

## `is not`

Returns `True` if both variables refer to different objects.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
```

**Output**

```python
True
```

---

## Difference Between `==` and `is`

| Operator | Purpose |
|----------|---------|
| `==` | Compares values |
| `is` | Compares object identity (memory location) |

### Example

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

**Output**

```python
True
False
```

> **Best Practice:** Use `is` and `is not` mainly for checking `None`.

```python
value = None

print(value is None)
print(value is not None)
```

---

# Membership Operators

Membership operators check whether an element exists in a sequence.

## Types

- `in`
- `not in`

---

## `in`

Returns `True` if the element exists.

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
```

**Output**

```python
True
```

---

## `not in`

Returns `True` if the element does not exist.

```python
print("orange" not in fruits)
```

**Output**

```python
True
```

---

## String Example

```python
language = "Python"

print("P" in language)
print("Java" in language)
```

**Output**

```python
True
False
```

---

## Uses

- Searching in lists
- Searching in strings
- Password validation
- Input validation

---

# Bitwise Operators

Bitwise operators work on the binary representation of numbers.

## Operators

| Operator | Meaning |
|----------|---------|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

---

## Binary Table (0–15)

| Decimal | Binary |
|---------:|:------:|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |
| 11 | 1011 |
| 12 | 1100 |
| 13 | 1101 |
| 14 | 1110 |
| 15 | 1111 |

---

## Bitwise AND (`&`)

Returns `1` only if both bits are `1`.

```python
print(5 & 3)
```

```
5 = 101
3 = 011
---------
    001
```

**Output**

```python
1
```

---

## Bitwise OR (`|`)

Returns `1` if at least one bit is `1`.

```python
print(5 | 3)
```

```
101
011
---
111
```

**Output**

```python
7
```

---

## Bitwise XOR (`^`)

Returns `1` if the bits are different.

```python
print(5 ^ 3)
```

```
101
011
---
110
```

**Output**

```python
6
```

---

## Bitwise NOT (`~`)

Flips all bits.

```python
print(~5)
```

**Output**

```python
-6
```

---

## Left Shift (`<<`)

Moves bits to the left.

```python
print(5 << 1)
```

**Output**

```python
10
```

**Rule**

- `<< 1` → Multiply by 2
- `<< 2` → Multiply by 4

---

## Right Shift (`>>`)

Moves bits to the right.

```python
print(5 >> 1)
```

**Output**

```python
2
```

**Rule**

- `>> 1` → Integer divide by 2

---

# Summary

## Logical Operators

- `and` → All conditions must be `True`.
- `or` → At least one condition must be `True`.
- `not` → Reverses the result.

---

## Identity Operators

- `is` → Checks if two variables refer to the same object.
- `is not` → Checks if two variables refer to different objects.

---

## Membership Operators

- `in` → Checks whether an element exists.
- `not in` → Checks whether an element does not exist.

---

## Bitwise Operators

- `&` → AND
- `|` → OR
- `^` → XOR
- `~` → NOT
- `<<` → Left Shift
- `>>` → Right Shift

---

# Interview Tips

- Use `==` to compare values.
- Use `is` and `is not` mainly with `None`.
- Use `in` for searching in strings and collections.
- Bitwise operators are useful in low-level programming, optimization, and some interview questions, but they are less common in everyday Python backend development.

---

# Status
