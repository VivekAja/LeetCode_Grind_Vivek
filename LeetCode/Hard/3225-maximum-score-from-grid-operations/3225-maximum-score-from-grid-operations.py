class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        prefix = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                prefix[c][r + 1] = prefix[c][r] + grid[r][c]
        pick = [0] * (n + 1)
        skip = [0] * (n + 1)

        for j in range(1, n):
            new_pick = [0] * (n + 1)
            new_skip = [0] * (n + 1)

            for curr in range(n + 1):
                for prev in range(n + 1):
                    if curr > prev:
                        
                        score = prefix[j - 1][curr] - prefix[j - 1][prev]
                        new_pick[curr] = max(new_pick[curr], skip[prev] + score)
                        new_skip[curr] = max(new_skip[curr], skip[prev] + score)
                    else:
                        
                        score = prefix[j][prev] - prefix[j][curr]
                        new_pick[curr] = max(new_pick[curr], pick[prev] + score)
                        new_skip[curr] = max(new_skip[curr], pick[prev])

            pick, skip = new_pick, new_skip

        return max(pick)