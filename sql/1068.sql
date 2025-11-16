'''
https://leetcode.com/problems/product-sales-analysis-i/?envType=study-plan-v2&envId=top-sql-50

ON IN THE QUERY TELLS US HOW TO JOIN 2 TABLES COMPARING FIELDS
'''

-- Write your PostgreSQL query statement below
SELECT P.PRODUCT_NAME, S.YEAR, S.PRICE
FROM SALES AS S
LEFT JOIN PRODUCT AS P
ON S.PRODUCT_ID = P.PRODUCT_ID
 