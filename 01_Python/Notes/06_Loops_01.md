# Day 05 – Python Loops

## What are Loops?

Loops are used to execute a block of code repeatedly without writing the same code multiple times.

Python provides two types of loops:

* `for` loop
* `while` loop

---

# 1. `for` Loop

A `for` loop is used when the number of iterations is known.

## Syntax

```python
for variable in sequence:
    # Code
```

### Example

```python
for i in range(5):
    print(i)
```

**Output**

```
0
1
2
3
4
```

---

# 2. The `range()` Function

`range()` generates a sequence of numbers.

## Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### Examples

```python
range(5)
```

Output:

```
0 1 2 3 4
```

```python
range(1, 6)
```

Output:

```
1 2 3 4 5
```

```python
range(2, 11, 2)
```

Output:

```
2 4 6 8 10
```

```python
range(10, 0, -1)
```

Output:

```
10 9 8 7 6 5 4 3 2 1
```

---

# 3. `while` Loop

A `while` loop executes as long as the given condition is `True`.

## Syntax

```python
while condition:
    # Code
```

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output

```
1
2
3
4
5
```

---

# Difference Between `for` and `while`

| `for` Loop                                  | `while` Loop                                                |
| ------------------------------------------- | ----------------------------------------------------------- |
| Used when the number of iterations is known | Used when the number of iterations is unknown               |
| Iterates over a sequence                    | Runs until a condition becomes False                        |
| Less chance of an infinite loop             | Can become an infinite loop if the condition is not updated |

---

# Practice Questions

1. Print numbers from **1 to 20**.
2. Print even numbers from **1 to 50**.
3. Print odd numbers from **1 to 50**.
4. Print numbers from **20 to 1**.
5. Print the multiplication table of **7**.
6. Find the sum of numbers from **1 to 100**.
7. Print the squares of numbers from **1 to 10**.
8. Print each character of your name.
9. Print numbers from **1 to 10** using a `while` loop.
10. Print even numbers from **2 to 20** using a `while` loop.

---

# Key Points

* Use `for` when the number of iterations is known.
* Use `while` when execution depends on a condition.
* `range()` is commonly used with `for` loops.
* Always update the loop variable in a `while` loop to avoid an infinite loop.
* Prefer descriptive variable names such as `total` instead of `sum` to avoid shadowing Python's built-in `sum()` function.

---

# Next Topic

* `break`
* `continue`
* `pass`
* Nested Loops
* Pattern Printing
* String Methods
