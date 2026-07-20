# SQL Special Operators

## What are Special Operators?

Special operators are used to filter data using ranges, lists, patterns, and NULL values.

---

## 1. IN

Returns rows that match any value in a list.

Example:

```sql
SELECT *
FROM employees
WHERE department IN ('IT', 'HR');
```

---

## 2. NOT IN

Returns rows that do not match any value in a list.

```sql
SELECT *
FROM employees
WHERE department NOT IN ('IT');
```

---

## 3. BETWEEN

Returns values within a range (inclusive).

```sql
SELECT *
FROM employees
WHERE salary BETWEEN 25000 AND 50000;
```

---

## 4. NOT BETWEEN

Returns values outside the given range.

```sql
SELECT *
FROM employees
WHERE salary NOT BETWEEN 30000 AND 45000;
```

---

## 5. LIKE

Used for pattern matching.

Starts with P

```sql
WHERE name LIKE 'P%';
```

Ends with l

```sql
WHERE name LIKE '%l';
```

Contains ha

```sql
WHERE name LIKE '%ha%';
```

Second character is r

```sql
WHERE name LIKE '_r%';
```

### Wildcards

- `%` → Any number of characters
- `_` → Exactly one character

---

## 6. NOT LIKE

Returns rows that do not match the pattern.

```sql
SELECT *
FROM employees
WHERE name NOT LIKE 'A%';
```

---

## 7. IS NULL

Returns rows where a column contains NULL.

```sql
SELECT *
FROM students
WHERE city IS NULL;
```

---

## 8. IS NOT NULL

Returns rows where a column is not NULL.

```sql
SELECT *
FROM students
WHERE city IS NOT NULL;
```

---

## Summary

| Operator | Purpose |
|----------|---------|
| IN | Matches values from a list |
| NOT IN | Excludes values from a list |
| BETWEEN | Checks values within a range |
| NOT BETWEEN | Checks values outside a range |
| LIKE | Pattern matching |
| NOT LIKE | Opposite of LIKE |
| IS NULL | Finds NULL values |
| IS NOT NULL | Finds non-NULL values |

---

## Key Points

- BETWEEN includes both start and end values.
- LIKE uses `%` and `_` wildcards.
- IN is a cleaner alternative to multiple OR conditions.
- IS NULL checks missing values.
- IS NOT NULL checks existing values.