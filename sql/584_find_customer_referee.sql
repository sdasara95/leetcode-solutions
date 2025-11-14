'''
This can be solved in multiple ways in Postgres

col != val is same as col <> val in Postgres
We can also use col is distinct from val
'''

SELECT NAME 
FROM CUSTOMER
WHERE REFEREE_ID IS DISTINCT FROM 2

SELECT NAME 
FROM CUSTOMER
WHERE (REFEREE_ID <> 2) OR REFEREE_ID IS NULL

SELECT NAME 
FROM CUSTOMER
WHERE (REFEREE_ID != 2) OR REFEREE_ID IS NULL