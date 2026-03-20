-- Sample SQL Query: Data Extraction for Food Supply Analysis
--
-- Purpose:
-- Retrieves cleaned, item-level inventory data for a specific food shelf
-- within a defined time range. This dataset serves as the foundation for
-- downstream aggregation and dashboard analysis.
--
-- Key Logic:
-- - Joins inventory records with shelf, category, and item type reference tables
-- - Filters data by food bank, shelf identifier, and date range
-- - Calculates total cost by combining item sales and delivery fees
-- - Enriches raw records with standardized category and item type labels
--
-- Use Case:
-- This query supports detailed analysis of inventory distribution and cost
-- structure, and is used as an intermediate dataset for Tableau visualization.

SELECT
    i.record_date,
    i.item_id,
    i.item_description,
    i.total_weight,
    i.total_sales,
    i.delivery_fee,
    i.category_code,
    i.total_sales + i.delivery_fee AS total_cost,
    c.category_name,
    t.item_type_name
FROM inventory_items i
JOIN shelf_reference s
    ON i.shelf_key = s.shelf_key
    AND i.bank_key = s.bank_key
LEFT JOIN category_lookup c
    ON i.category_key = c.category_key
LEFT JOIN item_type_lookup t
    ON i.type_key = t.type_key
WHERE i.bank_key = 1
    AND (
        s.shelf_number = 'SAMPLE-001'
        OR s.legacy_shelf_number = 'SAMPLE-001'
    )
    AND i.record_date BETWEEN DATE '2023-01-01' AND DATE '2025-12-31';
