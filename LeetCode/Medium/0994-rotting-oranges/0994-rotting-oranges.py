class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        time = 0

        while queue:
            row, col, t = queue.popleft()
            for dr, dc in directions:
                r = row+dr
                c = col+dc
                if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1
                    queue.append((r, c, t+1))
                    time = t+1
        return time if fresh == 0 else -1


            
        