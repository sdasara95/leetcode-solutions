'''
https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150

This problem description is vague so that confuses you at first.
Basically a region of Os that don't touch edges are considered surrounded & have to be filled 
If we invert the problem then regions connected to Os on borders are safe
We use this intuition to first parse border rows columns and mark connected O cells as safe
All the remaining Os have to be converted to X
Now convert back the Ss to Os

The loop on row column borders is where you might go wrong
We can use either dfs or bfs doesn't matter

Changing values of O to X and S to O is basic double nested for loop
'''

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])

        def dfs(row, col, board):
            if row not in range(0,M) or col not in range(0,N):
                return
            
            val = board[row][col]
            if val != "O":
                return
            
            board[row][col] = "S"

            dfs(row+1, col, board)
            dfs(row-1, col, board)
            dfs(row, col+1, board)
            dfs(row, col-1, board)

        for row in [0, M-1]:
            for col in range(0,N):
                val = board[row][col]
                if val == "O":
                    dfs(row, col, board)
        
        for col in [0, N-1]:
            for row in range(0,M):
                val = board[row][col]
                if val == "O":
                    dfs(row, col, board)

        for row in range(0, M):
            for col in range(0, N):
                val = board[row][col]
                if val == "O":
                    board[row][col] = "X"

                elif val == "S":
                    board[row][col] = "O"
        
        return board

    def print_board(self, board: List[List[str]]):
        for r in range(len(board)):
            print(board[r])

if __name__ == "__main__":
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.print_board(board)
    output = sol.solve(board)
    expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    print(output==expected)
    sol.print_board(output)