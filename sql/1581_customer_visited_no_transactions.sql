'''
https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan-v2&envId=top-sql-50

Always remember that you do group by on a column which has multiple values for other fields
That way you are collapsing it in a group with each cardinal column value
The collapsing is an aggregation
In select you can only display the collapsed column with unique values post group by
The aggregations like count for each unique column value can also be selected
You cannot have another column displayed after group by
What columns you have in group by clause, only they can be displayed using select
'''

-- Write your PostgreSQL query statement below
SELECT V.CUSTOMER_ID AS CUSTOMER_ID, COUNT(V.VISIT_ID) AS COUNT_NO_TRANS
FROM VISITS AS V
LEFT JOIN TRANSACTIONS AS T
ON V.VISIT_ID = T.VISIT_ID
WHERE T.TRANSACTION_ID IS NULL
GROUP BY V.CUSTOMER_ID;