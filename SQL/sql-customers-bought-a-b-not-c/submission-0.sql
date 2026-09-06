SELECT 
    c.customer_id, 
    c.customer_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.product_name IN ('A', 'B')  -- Only look at their purchases of A and B
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT o.product_name) = 2  -- Ensure they bought BOTH A and B
  AND c.customer_id NOT IN (             -- Ensure they never bought C
      SELECT customer_id 
      FROM orders 
      WHERE product_name = 'C'
  );