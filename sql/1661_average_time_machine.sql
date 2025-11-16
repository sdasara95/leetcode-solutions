'''
https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

Here an ENUM can have a fixed set of values
We use a simple = operator to check for Enum values

When we use - operator we need to cast it as NUMERIC which we can do two ways
The :: is type case operator in Postgres
'''

SELECT A1.MACHINE_ID, ROUND(AVG(A2.TIMESTAMP - A1.TIMESTAMP)::NUMERIC,3) AS PROCESSING_TIME
-- SELECT A1.MACHINE_ID, ROUND(AVG(CAST(A2.TIMESTAMP - A1.TIMESTAMP AS NUMERIC)),3) AS PROCESSING_TIME
FROM ACTIVITY AS A1
JOIN ACTIVITY AS A2
ON A1.MACHINE_ID = A2.MACHINE_ID
   AND A1.PROCESS_ID = A2.PROCESS_ID
   AND A1.ACTIVITY_TYPE = 'start'
   AND A2.ACTIVITY_TYPE = 'end'
GROUP BY A1.MACHINE_ID;


