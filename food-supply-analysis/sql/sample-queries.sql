SELECT
    c.category_name,
    SUM(i.total_sales + i.delivery_fee) AS total_cost,
    SUM(i.total_weight) AS total_weight
FROM inventory_items i
JOIN shelf_reference s
    ON i.shelf_key = s.shelf_key
    AND i.bank_key = s.bank_key
LEFT JOIN category_lookup c
    ON i.category_key = c.category_key
WHERE i.bank_key = 1
    AND s.shelf_number = 'SAMPLE-001'
    AND i.record_date BETWEEN DATE '2023-01-01' AND DATE '2025-12-31'
GROUP BY c.category_name
ORDER BY total_cost DESC;
