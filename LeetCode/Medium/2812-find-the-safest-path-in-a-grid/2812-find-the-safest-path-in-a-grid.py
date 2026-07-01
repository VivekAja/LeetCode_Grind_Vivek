from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        safe = [[ -1 for i in range(n)] for i in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safe[i][j] = 0
                    q.append((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safe[nr][nc] == -1:
                    safe[nr][nc] = safe[r][c] + 1
                    q.append((nr, nc))

        heap = [(-safe[0][0], 0, 0)]
        best = [[-1 for _ in range(n)] for _ in range(n)]
        best[0][0] = safe[0][0]
        while heap:
            neg_dist, r, c = heapq.heappop(heap)
            dist = -neg_dist
            if dist < best[r][c]:
                continue
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_dist = min(dist, safe[nr][nc])
                    if new_dist > best[nr][nc]:
                        best[nr][nc] = new_dist
                        heapq.heappush(heap, (-new_dist, nr, nc))