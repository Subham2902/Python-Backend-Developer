-- Aggregate Functions

-- 1. COUNT()

-- 1. Count all employees
SELECT COUNT(*)
FROM employees;

-- 2. Count non-NULL salaries
SELECT COUNT(salary)
FROM employees;

-- 3. Count employees in IT department
SELECT COUNT(*)
FROM employees
WHERE department = 'IT';

-- 4. Count employees with salary greater than 4000
SELECT COUNT(*)
FROM employees
WHERE salary > 40000;

-- 5. Count distinct department 
SELECT COUNT(DISTINCT department)
FROM employees;

-- PRACTICE QUESTIONS 

-- 1. Count all employees.
SELECT COUNT(*)
FROM employees;

-- 2. Count employees whose salary is greater than 30,000.
SELECT COUNT(*)
FROM employees
WHERE salary > 30000;

-- 3. Count employees in the HR department.
SELECT COUNT(*)
FROM employees
WHERE department = 'HR';

-- 4. Count distinct departments.
SELECT COUNT(DISTINCT(department))
FROM employees;

-- 🎯 Practice Challenge (Interview Level)

-- 1. Count employees whose salary is between 30,000 and 50,000.
SELECT COUNT(*)
FROM employees
WHERE salary BETWEEN 30000 AND 50000;

-- 2. Count employees whose department is IT or HR.
SELECT COUNT(*)
FROM employees
WHERE department IN ('IT', 'HR');

-- 3. Count employees whose name starts with 'R'.
SELECT COUNT(*)
FROM employees
WHERE name LIKE('R%');

-- 4. Count employees whose salary is NOT NULL.
SELECT COUNT(*)
FROM employees
WHERE salary is NOT NULL;
