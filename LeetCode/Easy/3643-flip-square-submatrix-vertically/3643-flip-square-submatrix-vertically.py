class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        startR = x
        endR = x+k-1

        startC = y
        endC = y+k-1

        for i in range(startR, x + k):
            for j in range(startC, endC + 1):
                grid[i][j], grid[endR][j] = grid[endR][j], grid[i][j]
            endR -= 1
            if i >= endR:
                break
        return grid