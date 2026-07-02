from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        maxx = [[-1] * n for _ in range(m)]
        start = health - grid[0][0]
        if start<=0:
            return False
        q = deque([(0,0, start)])
        maxx[0][0] = start

        while q:
            r, c, h = q.popleft()
            if r == m-1 and c == n-1 and h>=1:
                return True
            if h < maxx[r][c]:
                continue
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]

                    if nh > 0 and nh > maxx[nr][nc]:
                        maxx[nr][nc] = nh

                        if grid[nr][nc]== 0:
                            q.appendleft((nr, nc, nh))
                        else:
                            q.append((nr,nc,nh))
        return False

