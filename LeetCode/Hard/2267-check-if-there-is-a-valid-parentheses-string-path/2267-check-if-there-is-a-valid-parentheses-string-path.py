from collections import deque
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ')' or grid[m-1][n-1] == '(' or (m+n-1) % 2 != 0:
            return False

        queue = deque()
        queue.append((0,0,1))

        visited = set()
        visited.add((0,0,1))

        while queue:

            r,c, balance = queue.popleft()

            for dr, dc in [(0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc

                if nr >= m or nc >= n:
                    continue

                if nr < m and nc < n:
                    if grid[nr][nc] == "(":
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1
                
                if new_balance < 0:
                    continue

                if (m - 1 - nr) + (n - 1 - nc) < new_balance:
                    continue


                if nr == m-1 and nc == n-1 and new_balance == 0:
                    return True   
                             
                if (nr, nc,new_balance) not in visited:
                    visited.add((nr, nc, new_balance))
                    queue.append((nr, nc, new_balance))


        return False