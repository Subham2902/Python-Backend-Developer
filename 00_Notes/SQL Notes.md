# SQL Notes

# Chapter 1: Introduction to SQL

## What is SQL?

### Definition
SQL (Structured Query Language) is a standard language used to communicate with relational databases. It is used to retrieve, insert, update, and delete data from a database.

---

## Why do we use SQL?

SQL helps us:
- Retrieve data
- Insert new data
- Update existing data
- Delete unwanted data
- Create databases and tables

---

## Real-Life Example

Imagine a school database.

| Student_ID | Name | Age | Branch |
|------------|------|-----|--------|
|101|Rahul|21|CSE|
|102|Priya|22|ECE|

If the principal wants to see all students, SQL can retrieve the data instantly.

---

## Interview Answer

**Q. What is SQL?**

**Answer:**

SQL (Structured Query Language) is a standard language used to communicate with relational databases. It is used to retrieve, insert, update, and delete data efficiently.

---

# Database

## Definition

A Database is an organized collection of related data stored electronically.

### Example

A college stores:
- Student Details
- Faculty Details
- Attendance
- Marks

All of this information is stored inside a database.

---

# Table

## Definition

A Table is a collection of related data arranged in rows and columns.

Example:

| ID | Name | Salary |
|----|------|--------|
|1|Amit|50000|
|2|Riya|60000|

---

# Row

A Row represents one complete record in a table.

Example:

|1|Amit|50000|

This entire line is one row.

---

# Column

A Column represents one attribute (field) of the data.

Examples:
- ID
- Name
- Salary

---

# SELECT Statement

## Definition

The SELECT statement is used to retrieve data from a table.

## Syntax

```sql
SELECT * FROM employees;
```

---

## Line-by-Line Explanation

### SELECT

Used to retrieve data from a database.

### *

Means "Select all columns."

### FROM

Specifies the table from which data should be retrieved.

### employees

Name of the table.

---

## Complete Meaning

```sql
SELECT * FROM employees;
```

This query retrieves all rows and all columns from the employees table.

---

# Key Points

✔ SQL is used to communicate with databases.

✔ A database stores related data.

✔ A table contains rows and columns.

✔ SELECT retrieves data.

✔ FROM specifies the table.

✔ * means all columns.

---

# Interview Questions

1. What is SQL?
2. What is a database?
3. What is a table?
4. What is a row?
5. What is a column?
6. What does SELECT do?
7. What does * mean?
8. What does FROM do?

---

# Practice

```sql
SELECT * FROM employees;

SELECT * FROM pizzas;

SELECT * FROM orders;
```

---

# Revision

- SQL = Structured Query Language
- Used to communicate with relational databases.
- SELECT retrieves data.
- FROM specifies the table.
- * means all columns.


# My Understanding

- SQL is used to communicate with databases.
- SELECT is used to retrieve data.
- * means all columns.
- FROM tells SQL which table to use.

### Doubts
- Difference between DBMS and RDBMS?
- Why do we use * instead of column names?