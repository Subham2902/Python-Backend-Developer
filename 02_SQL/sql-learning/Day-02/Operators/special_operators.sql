-- SPECIAL OPERATORS 
-- IN Operators

SELECT * 
FROM employees
WHERE department IN ('HR', 'IT');

-- NOT IN Operators

SELECT *
FROM employees
WHERE department NOT IN ('HR');

-- BETWEEN Operators

SELECT *
FROM employees
WHERE salary BETWEEN 30000 AND 50000;

-- NOT BETWEEN 

SELECT *
FROM employeeS
WHERE salary NOT BETWEEN 30000 AND 50000;

-- LIKE Operators

SELECT *
FROM employees
WHERE name LIKE 'R%';

SELECT *
FROM employees
WHERE name LIKE '%a';

SELECT *
FROM employees
WHERE name LIKE '%it%';

SELECT *
FROM employees
WHERE name LIKE '_r%';

SELECT *
FROM employees
WHERE name LIKE '__h__';

-- NOT LIKE Operators

SELECT *
FROM employees
WHERE name NOT LIKE 'R%';

-- IS NULL 

SELECT *
FROM students 
WHERE city IS NULL;

-- IS NOT NULL

SELECT *
FROM students 
WHERE city IS NOT NULL;

-- PRACTICE QUESTIONS --
-- 1. Show employees from HR and Sales.

SELECT *
FROM employees
WHERE department IN ('HR', 'Sales');

-- 2. Show employees not from IT.

SELECT * 
FROM employees 
WHERE department NOT IN ('IT');

-- 3. Find employees with salary between 25000 and 50000.

SELECT *
FROM employees
WHERE salary BETWEEN 25000 AND 50000;

-- 4. Find employees with salary not between 30000 and 45000.

SELECT * 
FROM employees
WHERE salary NOT BETWEEN 30000 AND 45000;

-- 5. Find employees whose name starts with P.

SELECT * 
FROM employees
WHERE name LIKE 'P%';

-- 6. Find employees whose name ends with l.

SELECT *
FROM employees
WHERE name LIKE '%l';

-- 7. Find employees whose name contains ha.

SELECT *
FROM employees
WHERE name LIKE '%ha%';

-- 8. Find employees whose department is IT or HR using IN.

SELECT *
FROM employees 
WHERE department IN ('IT', 'HR');

-- 9. Find employees whose name does not start with A.

SELECT *
FROM employees
WHERE name NOT LIKE 'A%';

-- 10. Find student whose city is NULL.

SELECT * 
FROM students 
WHERE city IS NULL;