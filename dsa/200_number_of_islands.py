'''
https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150

In this quesiton you can traverse the graph using bfs or dfs
Since level order is not necessary let's do dfs as lesser code.

for each row column element in the graph we do dfs traversal if it's 1 & not visited before
If it's 0 we just skip
We are only interested in finding all 1 neighbors for an unseen 1 valued row column
It's neighboring 1s will get taken care in dfs traversal and put in visited Set
We increase count only when we come across an unseen 1 whose neighbors not visited
We cannot have an unseen one with visited neighbors as dfs would have visited it too

Time complexity will be O(M x N)
This is because each element we do atmost 4 or 8 neighbor checks which is O(1)
'''

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        seen = set()
        total = 0

        def dfs(row, col, grid):

            if (row, col) in seen or grid[row][col] == "0":
                return
            
            seen.add((row, col))

            val = grid[row][col]

            directions = ((1,0),(-1,0),(0,1),(0,-1))
            for dx, dy in directions:
                if 0 <= row+dx < M and 0 <= col+dy < N and grid[row+dx][col+dy]=="1":
                    dfs(row+dx, col+dy, grid)

        for row in range(M):
            for col in range(N):
                if grid[row][col] == "1" and (row, col) not in seen:
                    total += 1
                    dfs(row, col, grid)
        return total

if __name__ == "__main__":
    sol = Solution()

    # answer is 1
    print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

    # answer is 3
    print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
