'''
https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

This dataset is of temperature and date for a day
We need to return ids for days which were hotter than previous days

We do a join of the Weather table with itself 
JOIN = “Cartesian product + filtering with ON condition”
FULL JOIN = JOIN + UNMATCHED A ROWS + UNMATCHED B ROWS
Remember that FULL JOIN is not a full cartesian product
FULL JOIN does not do cartesian product for unmatched A rows and B rows 
That is why FULL JOIN is not cartesian product

We do JOIN as we need NON NULL DATE for both DATE fields to compare 
'''

-- Write your PostgreSQL query statement below

SELECT W1.ID
FROM WEATHER AS W1
JOIN WEATHER AS W2
ON W1.RECORDDATE - 1 = W2.RECORDDATE
WHERE W1.TEMPERATURE > W2.TEMPERATURE