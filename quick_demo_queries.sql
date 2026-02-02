-- [MENU ITEMS]
SELECT m.name as 'Dish', c.category_name as 'Category', m.price, m.status 
FROM menu_items m
LEFT JOIN menu_categories c ON m.category_id = c.category_id;

-- [STOCKS]
SELECT m.name as 'Item', i.quantity as 'Current Stock', i.reorder_level as 'Alert Level'
FROM inventory i
JOIN menu_items m ON i.menu_item_id = m.menu_item_id;

-- [SALES]
SELECT order_id, order_date, total_amount, status 
FROM orders 
ORDER BY order_date DESC;

-- [STAFF]
SELECT name, job_role, phone, is_active 
FROM staff;

-- [FEEDBACK]
SELECT c.name as 'Customer', f.rating, f.comment, f.feedback_date
FROM feedback f
JOIN customers c ON f.customer_id = c.customer_id;

-- [TABLES]
SELECT table_no, capacity, status 
FROM restaurant_tables;

-- [BEST SELLERS]
SELECT m.name, SUM(oi.quantity) as 'Total Sold'
FROM order_items oi
JOIN menu_items m ON oi.menu_item_id = m.menu_item_id
GROUP BY m.name
ORDER BY SUM(oi.quantity) DESC;
