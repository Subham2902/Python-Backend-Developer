# SQL Learning - Day 1

# What is SQL?

SQL (Structured Query Language) is the standard language used to communicate with relational databases. It is used to store, retrieve, update, and delete data efficiently.

SQL is one of the most important skills for Backend Developers, Data Analysts, Data Engineers, and Database Administrators.

---

# What is PostgreSQL?

PostgreSQL is a powerful, open-source Relational Database Management System (RDBMS). It stores data in tables and allows us to manage that data using SQL.

---

# Why Learn SQL?

- Store and manage data
- Retrieve information quickly
- Build backend applications
- Analyze business data
- Essential for technical interviews
- Used by almost every software company

---

# Database Concepts

## Database
A database is an organized collection of related data.

Example:
A company's employee records.

---

## Table

A table stores data in rows and columns.

Example:

| id | name | age | department | salary |
|----|------|-----|------------|--------|

---

## Row (Record)

A single entry in a table.

Example:

Rahul | 24 | IT | 45000

---

## Column

A column stores one type of information.

Examples:

- id
- name
- age
- department
- salary

---

# What We Did Today

## 1. Installed PostgreSQL 18

Verified installation using:

```bash
psql --version
```

---

## 2. Opened pgAdmin 4

Connected to the PostgreSQL server.

---

## 3. Created Database

```sql
CREATE DATABASE sql_learning;
```

---

## 4. Created Table

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);
```

---

## 5. Inserted Records

Used the INSERT INTO statement to add employee data into the table.

---

## 6. Learned SELECT

Used to retrieve data.

Example:

```sql
SELECT * FROM employees;
```

---

## 7. Learned WHERE

Filters rows based on a condition.

Example:

```sql
SELECT *
FROM employees
WHERE age > 25;
```

---

## 8. Learned ORDER BY

Sorts the data.

Ascending:

```sql
ORDER BY age ASC;
```

Descending:

```sql
ORDER BY salary DESC;
```

---

## 9. Learned LIMIT

Returns only a specified number of rows.

Example:

```sql
SELECT *
FROM employees
LIMIT 3;
```

---

# SQL Keywords Learned

- CREATE DATABASE
- CREATE TABLE
- INSERT INTO
- SELECT
- FROM
- WHERE
- ORDER BY
- ASC
- DESC
- LIMIT

---

# Key Takeaways

- SQL is used to communicate with databases.
- PostgreSQL is a Relational Database Management System.
- Data is stored in tables.
- Tables consist of rows and columns.
- SELECT retrieves data.
- WHERE filters data.
- ORDER BY sorts data.
- LIMIT restricts the number of returned rows.

---

# Day 1 Summary

✅ Installed PostgreSQL

✅ Configured pgAdmin

✅ Created a database

✅ Created a table

✅ Inserted data

✅ Executed basic SQL queries

---

# Next Topics

- UPDATE
- DELETE
- DISTINCT
- AND
- OR
- NOT
- LIKE
- IN
- BETWEEN