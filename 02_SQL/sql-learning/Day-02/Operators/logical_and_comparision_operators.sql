-- SQL operators --

-- Comparision Operators --

-- 1. Equal to(=) operators
SELECT * FROM employees
WHERE department = 'IT';

-- 2. Not Equal() operators 
SELECT * FROM employees
WHERE department != 'IT';

-- 3. Greater Than(>) operators
SELECT * FROM employees 
WHERE salary > 50000;

-- 4. Less Than(<) operators 
SELECT * FROM employees
WHERE age < 25;

-- 5. Greater Than or Equal (>=) operators
SELECT * FROM employees
WHERE salary >= 50000;

-- 6. Less Than or Equal(<=) operators
SELECT * FROM employees 
WHERE age <= 25;

-- PRACTICE QUESTIONS ---
-- Q1. Show all employees whose salary is greater than 45,000.
SELECT * FROM employees
WHERE salary > 45000;

-- Q2. Show employees whose age is less than 25.
SELECT * FROM employees
WHERE age < 25;

--Q3. Display employees whose salary is greater than or equal to 50,000.
SELECT * FROM employees
WHERE salary >= 50000;


--Q4. Show employees whose department is IT.
SELECT * FROM employees
WHERE department = 'IT';

--Q5. Show employees whose department is not HR.
SELECT * FROM employees
WHERE department != 'HR';

--Q6. Display employees whose age is exactly 28.
SELECT * FROM employees
WHERE age = 28;

--Q7. Show employees whose salary is less than or equal to 48,000.
SELECT * FROM employees
WHERE salary <= 48000;

--Q8. Display only the name and salary of employees whose salary is greater than 40,000.
SELECT name, salary 
FROM employees
WHERE salary > 40000;


-- Logical Operators --

-- 1. AND operator

SELECT * FROM employees
WHERE department = 'IT' AND salary > 45000;

-- 2. OR operator

SELECT * FROM employees
WHERE department = 'IT' 
OR department = 'HR';

-- 3. NOT operator

SELECT * FROM employees
WHERE NOT department = 'IT';

-- PRACTICE QUESTIONS 
--Q9. Show employees who belong to the IT department and have a salary greater than 45,000
SELECT *
FROM employees
WHERE department = 'IT' 
AND salary > 45000;

--Q10. Show employees who belong to HR or Finance.
SELECT *
FROM employees
WHERE department = 'HR' OR
department = 'Finance';

--Q11. Show employees who are not in the Sales department.
SELECT * 
FROM employees
WHERE  NOT department = 'Sales';

--Q12. Show employees whose age is greater than 24 and salary is less than 60,000.
SELECT * 
FROM employees
WHERE age >  24 
AND salary < 60000;

--Q13. Display the name and department of employees who are in IT or Sales.
SELECT name, department
FROM employees
WHERE department = 'IT'
OR department ='Sales';

--Q14. Show employees whose department is IT and age is greater than or equal to 24.
SELECT * 
FROM employees 
WHERE department = 'IT'
AND age >= 24;

--Q15. Show employees who are not in HR and whose salary is greater than 45,000.
SELECT * 
FROM employees
WHERE NOT department = 'HR'
AND salary > 45000;


-- CHALLANGE QUESTIONS --
-- Challenge 1
-- Show only:
-- name
-- department
-- salary

-- where:
-- department is IT
-- salary is greater than 45,000
-- age is less than 30

SELECT name , department, salary
FROM employees
WHERE department = 'IT'
AND salary > 45000
AND age < 30;

Challenge 2

-- Show employees who are either:
-- in Finance
-- OR
-- salary greater than 55,000

SELECT * 
FROM employees
WHERE department = 'Finance'
OR salary > 55000;

Challenge 3

-- Show employees who:
-- are not in IT
-- age is 25 or above
-- salary is less than 60,000
SELECT * 
FROM employees
WHERE department != 'IT'
AND age >= 25
AND salary < 60000;

-- Bonus Challenge ⭐--
-- Show employees who are not in HR or whose salary is greater than or equal to 60,000.
SELECT * 
FROM employees
WHERE NOT department ='HR'
OR salary >= 60000;
