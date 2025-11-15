'''
https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150

The intuition here is a/b * b/c = a/c

We don't need a node class to create a graph
Nested dictionary is enough to create graph
Use default dict with dict default, this way nested key lookup happens without errors
We also maintain a valid set to track all equation keys

We do a DFS to derive the equation
If key2 is not in graph[key1] then we return -1 which is invalid
If both are same we return 1
For each key, val item in graph[key1] we check if we can reach key2

There could be a cycle like a->b->c->a leading to infinite loop
To take care of this we need to pass a visited set to track all visited keys

If we get -1 we move on
If not -1 we multiply recursion result with current val in loop and return

We do this for every query which is why new visited set for each dfs function call
'''


from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        valid = set()
        for idx, equation in enumerate(equations):
            eq1, eq2 = equation
            valid.add(eq1)
            valid.add(eq2)
            graph[eq1][eq2] = values[idx]
            graph[eq2][eq1] = 1/values[idx]
        
        def dfs(key1, key2, visited):
            visited.add(key1)
            
            if key1 == key2:
                return 1
            
            for key, val in graph[key1].items():
                if key in visited:
                    continue
                
                res = dfs(key, key2, visited)
                if res!= -1:
                    return res * val
            
            return -1

        return [dfs(key1, key2, set()) if key1 in valid and key2 in valid \
                                else -1 \
                                for key1, key2 in queries]


if __name__ == "__main__":
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    solver = Solution()
    res = solver.calcEquation(equations, values, queries)
    print(res)
