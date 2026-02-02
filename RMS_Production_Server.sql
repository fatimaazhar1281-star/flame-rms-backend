# look menu
SELECT m.name as 'Dish Name', c.category_name as 'Category', m.price, m.status 
FROM menu_items m
LEFT JOIN menu_categories c ON m.category_id = c.category_id;

# check inventory
SELECT m.name as 'Item Name', i.quantity, i.unit, i.reorder_level
FROM inventory i
JOIN menu_items m ON i.menu_item_id = m.menu_item_id;

#see recent records
SELECT order_id, order_date, status, total_amount 
FROM orders 
ORDER BY order_date DESC;
