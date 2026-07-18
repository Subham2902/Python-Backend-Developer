# Day 2 - SQL Operators

## Topics Covered
- Comparison Operators
- Logical Operators
- Practice Questions
- Challenge Questions

---

# What are SQL Operators?

SQL operators are symbols or keywords used to perform operations on data. They are mainly used with the `WHERE` clause to filter records from a table.

Syntax:

```sql
SELECT column_name
FROM table_name
WHERE condition;
```

---

# 1. Comparison Operators

Comparison operators compare two values and return rows where the condition is TRUE.

| Operator | Meaning | Example |
|----------|---------|---------|
| = | Equal To | `age = 25` |
| != | Not Equal To | `department != 'IT'` |
| <> | Not Equal To (SQL Standard) | `salary <> 50000` |
| > | Greater Than | `salary > 50000` |
| < | Less Than | `age < 25` |
| >= | Greater Than or Equal To | `salary >= 50000` |
| <= | Less Than or Equal To | `age <= 25` |

### Example

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

---

# 2. Logical Operators

Logical operators combine multiple conditions.

## AND

Returns rows only if **all conditions are TRUE**.

```sql
SELECT *
FROM employees
WHERE department = 'IT'
AND salary > 45000;
```

---

## OR

Returns rows if **at least one condition is TRUE**.

```sql
SELECT *
FROM employees
WHERE department = 'IT'
OR salary > 45000;
```

---

## NOT

Reverses a condition.

```sql
SELECT *
FROM employees
WHERE NOT department = 'HR';
```

---

# Difference Between Comparison and Logical Operators

## Comparison Operators

- Compare one value with another.
- Return TRUE or FALSE.

Example:

```sql
salary > 50000
```

---

## Logical Operators

- Combine or reverse comparison conditions.
- Used with AND, OR and NOT.

Example:

```sql
department = 'IT'
AND salary > 45000;
```

---

# Important Interview Points

### Difference between AND and OR

**AND**
- Every condition must be TRUE.

**OR**
- At least one condition must be TRUE.

---

### Difference between != and <>

Both mean **Not Equal To**.

- `!=` is supported by PostgreSQL.
- `<>` is the SQL Standard.

---

# Queries Practiced

- SELECT
- WHERE
- Comparison Operators
- Logical Operators
- Practice Questions
- Challenge Questions

---

# Key Takeaways

- SQL operators help filter data.
- Comparison operators compare values.
- Logical operators combine multiple conditions.
- `AND` requires all conditions to be TRUE.
- `OR` requires at least one condition to be TRUE.
- `NOT` reverses a condition.

---

# Next Topic

- BETWEEN
- IN
- LIKE
- IS NULL
- DISTINCT