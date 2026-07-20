# SQL Data Types

## What are Data Types?

Data types define what kind of data can be stored in a column.

---

## Numeric Data Types

### INT
Stores whole numbers.

Example:
```sql
age INT
```

Example Values:
18, 25, 100

---

### DECIMAL(p,s)

Stores numbers with decimal values.

Example:
```sql
salary DECIMAL(10,2)
```

Example Values:
25000.50
49999.99

---

## Character Data Types

### CHAR(n)

Stores fixed-length text.

Example:
```sql
gender CHAR(1)
```

Example Values:
'M'
'F'

---

### VARCHAR(n)

Stores variable-length text.

Example:
```sql
name VARCHAR(100)
```

Example Values:
Rahul
Sneha
Rohan

---

## Date and Time Data Types

### DATE

Stores dates only.

Example:
```sql
joining_date DATE
```

Example Value:
2026-07-20

---

### TIME

Stores only time.

Example:
```sql
login_time TIME
```

---

### TIMESTAMP

Stores both date and time.

Example:
```sql
created_at TIMESTAMP
```

---

## Boolean Data Type

Stores TRUE or FALSE.

Example:
```sql
is_active BOOLEAN
```

---

## Common Data Types

| Data Type | Used For |
|-----------|-----------|
| INT | Whole numbers |
| DECIMAL | Decimal values |
| CHAR | Fixed-length text |
| VARCHAR | Variable-length text |
| DATE | Date |
| TIME | Time |
| TIMESTAMP | Date and Time |
| BOOLEAN | True/False |

---

## Summary

- INT → Whole numbers
- DECIMAL → Decimal numbers
- CHAR → Fixed-length text
- VARCHAR → Variable-length text
- DATE → Stores date
- TIME → Stores time
- TIMESTAMP → Stores date and time
- BOOLEAN → Stores TRUE/FALSE