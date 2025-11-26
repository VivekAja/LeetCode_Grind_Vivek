class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        self.M = 10**9 + 7
        self.m = len(grid)
        self.n = len(grid[0])
        self.k = k
        self.grid = grid
        self.memo = [[[-1] * k for _ in range(self.n)] for _ in range(self.m)]
        return self.solve(0, 0, 0)
    def solve(self, row: int, col: int, remain: int) -> int:
        if row >= self.m or col >= self.n:
            return 0
        if row == self.m - 1 and col == self.n - 1:
            final_sum_remainder = (remain + self.grid[row][col]) % self.k
            return 1 if final_sum_remainder == 0 else 0
        if self.memo[row][col][remain] != -1:
            return self.memo[row][col][remain]
        new_remain = (remain + self.grid[row][col]) % self.k
        down = self.solve(row + 1, col, new_remain)
        right = self.solve(row, col + 1, new_remain)
        result = (down + right) % self.M
        self.memo[row][col][remain] = result
        
        return result