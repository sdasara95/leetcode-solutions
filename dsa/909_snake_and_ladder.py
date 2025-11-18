'''
https://leetcode.com/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150


'''

from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # we do 1 based indexing for ease
        nrolls = [-1]*(n*n + 1) 
        nrolls[1] = 0
        q = deque([1])
        
        count = 0
        while q:
            curr = q.popleft()
            for i in range(1,7):
                nxt = curr + i

                if nxt > n*n:
                    break
                
                # do -1 to convert to 0 based index 
                row = (nxt-1) // n
                col = (nxt-1) % n
                val = board[n-1-row][n-1-col if row%2 else col]
                nxt_final = val if val > 0 else nxt

                if nxt_final == n*n:
                    return nrolls[curr] + 1 # curr rolls + 1

                if nrolls[nxt_final] == -1:
                    nrolls[nxt_final] = nrolls[curr] + 1 # curr rolls + 1
                    q.append(nxt_final)
        
        return -1

if __name__ == "__main__":
    solver = Solution()
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
    res = solver.snakesAndLadders(board)
    ans = 4
    print(res==4, res)


