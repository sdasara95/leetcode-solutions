'''
https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50

Use aliasing to prevent ambiguity
If you did SELECT UNIQUE_ID, NAME
It will work only if these columns dont exist in both the tables
If both table have their field Postgres will get confused on which to execute

We do left join to get all unique ids for employees table
We dont need joined rows for other tables

How left join works:
1) Scan all rows in left table
2) Find rows in right table matching based on join condition
3) Return only columns in SELECT from processed results
'''

-- Write your PostgreSQL query statement below

SELECT EU.UNIQUE_ID, E.NAME
FROM EMPLOYEES AS E
LEFT JOIN EMPLOYEEUNI AS EU
ON E.ID = EU.ID