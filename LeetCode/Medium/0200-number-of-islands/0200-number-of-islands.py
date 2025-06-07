class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        curr = 0
        def dfs(pos):
            i, j = pos
            directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                r = i + dr
                c = j + dc
                if r>=0 and r<m and c>=0 and c<n and grid[r][c] == '1':
                    grid[r][c] = '*'
                    dfs((r,c))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    curr += 1
                    grid[i][j] = '*'
                    dfs((i, j))

        return curr