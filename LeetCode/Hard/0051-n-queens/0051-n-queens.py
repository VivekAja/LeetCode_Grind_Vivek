class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posd = set() # row - col
        negd = set() # row + col

        res = []
        board = [["."] * n for i in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r - c in posd or r + c in negd:
                    continue
                col.add(c)
                posd.add(r-c)
                negd.add(r+c)
                board[r][c] = "Q"

                backtrack(r+1)
                # removing things
                col.remove(c)
                posd.remove(r-c)
                negd.remove(r+c)
                board[r][c] = "."


        backtrack(0)
        return res