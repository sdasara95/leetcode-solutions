'''
https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150

Remember that ordered dependency graph question i.e. DAG is topological sort problem
A node without dependency will have zero indegree if edge from prereq to course
However for ease of intuition we can even reverse the graph
That way the node in graph with no prereq will have zero outdegree
A node having dependency is an outdegree node
We first create a map of each prerequisite node and it's dependencies in list
We also have another map of each course node and it's number of outdegrees i.e dependencies

Now we take only the courses with 0 outdegrees ie zero dependencies
We then add them to a BFS Queue
We do BFS pop and check for all the courses depended on curr node
We reduce all the dependent course outdegree by 1 and if anyone becomes zero we add it to queue for BFS
Every time we do BFS pop we increase count

Finally we return True if count == number of courses

Idea of topological sort is dependent nodes should come later in traversal order
That's why this is for DAG and fails in case of Cycle in Graph

Indegree/Outdegree depends on how you want to solve this problem by representing dependencies

We can solve this problem with DFS also but we have to maintain current path during recursion 

BFS for Topological Sort is Kahn's Algorithm
'''

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}
        outdegree_map = {i:0 for i in range(numCourses)}

        for prereq in prerequisites:
            crs, pre = prereq
            pre_map[pre].append(crs)
            outdegree_map[crs] += 1
        
        q = deque([i for i in range(numCourses) if outdegree_map[i]==0])

        count = 0
        while q:
            crs = q.popleft()
            count += 1
            for dep in pre_map[crs]:
                outdegree_map[dep] -= 1
                if outdegree_map[dep] == 0:
                    q.append(dep)

        return count == numCourses

if __name__ == "__main__":
    solver = Solution()
    numCourses = 5
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    res = solver.canFinish(numCourses, prerequisites)
    print(res)


