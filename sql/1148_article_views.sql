```
https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=top-sql-50

Question is little vague 
The table has no primary keys
We need to return distinct author ids who viewed their articles

Order of execution is not same as what's written:
1. Where to filter docs
2. Order to process this filtered subset
3. Select from this processed subset
```

SELECT DISTINCT AUTHOR_ID AS ID
FROM VIEWS
WHERE AUTHOR_ID = VIEWER_ID
ORDER BY AUTHOR_ID ASC


