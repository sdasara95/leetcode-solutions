'''
https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50
'''

SELECT TWEET_ID 
FROM TWEETS
WHERE LENGTH(CONTENT) > 15