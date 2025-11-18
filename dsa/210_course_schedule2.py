'''
https://leetcode.com/problems/course-schedule-ii/?envType=study-plan-v2&envId=top-interview-150

This problem is same as 207_course_schedule.py
In this case we just have to return the TOPOLOGICAL SORT ORDER

Stick with BFS ie Kahn Algorithm for it

For ease of intuition model each dependency edge as an outdegree from dependent node
Consider all courses with no outdegree ie dependency and add them to queue
Do BFS and reduce outdegree of all its dependents by 1
We do this because it's like we're removing the independent node from the graph by popping it
If any of the dependents outdegree becomes zero add it to the queue & continue BFS

'''

from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i:[] for i in range(numCourses)}
        outdegree_map = {i:0 for i in range(numCourses)}

        for prereq in prerequisites:
            curr, pre = prereq
            pre_map[pre].append(curr)
            outdegree_map[curr] += 1
        
        q = deque([i for i in outdegree_map if outdegree_map[i]==0])

        output = []
        while q:
            crse = q.popleft()
            output.append(crse)
            for dep in pre_map[crse]:
                outdegree_map[dep] -= 1
                if outdegree_map[dep] == 0:
                    q.append(dep)
        
        if len(output) == numCourses:
            return output
        else:
            return []


if __name__ == "__main__":
    solver = Solution()
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 4
    res = solver.findOrder(numCourses, prerequisites)
    print(res)