CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employees(name, age, department, salary)
VALUES
('Rahul', 24, 'IT', 45000),
('Priya', 27, 'HR', 52000),
('Amit', 30, 'Finance', 60000),
('Neha', 25, 'IT', 50000),
('Rohan', 29, 'Sales', 55000);

SELECT * FROM employees;

SELECT name FROM employees;

SELECT * FROM employees
WHERE age > 25;

SELECT * FROM employees
WHERE department = 'IT';

SELECT * FROM employees
ORDER BY salary DESC;

SELECT * FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT * FROM employees 
WHERE salary > 50000;

SELECT * FROM employees 
WHERE age < 28;

SELECT name, salary 
FROM employees;

SELECT * FROM employees
ORDER BY age ASC;