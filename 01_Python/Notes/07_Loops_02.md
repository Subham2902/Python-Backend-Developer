# 4. break Statement

## Definition
The `break` statement is used to terminate a loop immediately when a specified condition becomes `True`.

When `break` is executed:
- The current loop stops.
- Control moves to the first statement after the loop.

### Syntax

```python
break
```

### Example

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

### Output

```
1
2
3
4
5
```

### Use Cases
- Searching for an item.
- Exiting a loop when the required result is found.
- Avoiding unnecessary iterations.

---

# 5. continue Statement

## Definition

The `continue` statement skips the current iteration of a loop and moves to the next iteration without terminating the loop.

### Syntax

```python
continue
```

### Example

```python
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
```

### Output

```
1
2
3
4
5
7
8
9
10
```

### Use Cases

- Ignore specific values.
- Skip invalid data.
- Continue processing remaining iterations.

---

# 6. pass Statement

## Definition

The `pass` statement is a placeholder that performs no action.

It is used when Python requires a statement syntactically, but you do not want to execute any code.

### Syntax

```python
pass
```

### Example

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

### Output

```
1
2
3
4
5
```

### Use Cases

- Empty loops
- Empty functions
- Empty classes
- Code that will be implemented later

---

# 7. Nested Loops

## Definition

A nested loop is a loop inside another loop.

- The outer loop controls the number of rows.
- The inner loop controls the number of iterations inside each row.

### Syntax

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

### Output

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

### Applications

- Pattern printing
- Matrix operations
- Tables
- Game development
- Grid-based problems

---

# 8. Pattern Printing (Basic)

Pattern printing is one of the best ways to understand nested loops.

### Star Pattern

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
```

Output

```
*
* *
* * *
* * * *
* * * * *
```

---

### Reverse Star Pattern

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output

```
* * * * *
* * * *
* * *
* *
*
```

---

### Number Pattern

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

Output

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### Repeated Number Pattern

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
```

Output

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

# Summary

- `break` → Stops the loop immediately.
- `continue` → Skips the current iteration.
- `pass` → Does nothing (placeholder).
- Nested loops → A loop inside another loop.
- Pattern printing → Practical application of nested loops.