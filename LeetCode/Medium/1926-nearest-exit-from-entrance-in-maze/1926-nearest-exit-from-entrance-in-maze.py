class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze[0])
        m = len(maze)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            row, col, step = queue.popleft()

            for dr, dc in directions:
                r = row+dr
                c = col+dc

                if 0<=r<m and 0<=c<n and maze[r][c] == "." and (r,c) not in visited:
                    if r in [0, m-1] or c in [0, n-1]:
                        return step + 1
                    queue.append((r,c, step+1))
                    visited.add((r,c))
        return -1

        """
        1. take 
        """