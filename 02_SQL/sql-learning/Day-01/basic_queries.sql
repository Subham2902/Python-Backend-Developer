SELECT DATABASE();

SHOW TABLES();

SELECT *
FROM orders;

SELECT order_id, order_date
FROM orders;

SELECT *
FROM orders
WHERE order_date = '2015-01-01';