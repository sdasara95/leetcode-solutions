'''
https://leetcode.com/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150

This problem can be solved with both dfs and bfs.
If we do bfs we don't need to do level based bfs with for loop inside while loop
Simple bfs is enough to visit all nodes once
We add neighbor node to queue only if we haven't visited it before
This way we ensure each node is visited atleast once
Also for the first node, we need to put it into the dict initially as it won't exist
We can do it through dict initialisation or with an if condition inside while loop

Whether unidirectional or bidirectional graph this code will work as we need to visit only once

Be careful of recloning node errors if we don't check for visited using hashmap

Remember except the initial node we don't need to copy current nodes
We only copy neighbors and do their bfs
The current node must have already gotten copied in previous loop iteration as neighbor
'''

from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = dict()
        # old_to_new = {node : Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()
            
            # This line of code is only needed for the first time we see input node
            if curr not in old_to_new:
                old_to_new[curr] = Node(curr.val)

            for nei in curr.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)
                old_to_new[curr].neighbors.append(old_to_new[nei])
        
        return old_to_new[node]

if __name__ == "__main__":
    # Example graph: 1 -- 2
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]

    solver = Solution()
    clone = solver.cloneGraph(n1)

    print("Original node:", n1, "Neighbors:", [n.val for n in n1.neighbors])
    print("Cloned node:", clone, "Neighbors:", [n.val for n in clone.neighbors])