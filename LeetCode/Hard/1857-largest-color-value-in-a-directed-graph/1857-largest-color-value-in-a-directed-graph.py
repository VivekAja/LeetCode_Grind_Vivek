#DFS
# Time: O(N+E)
# Space: 

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        def dfs(node):
            if node in path:
                return float("inf")
            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorIndex = int(ord(colors[node][0]) - ord("a"))
            count[node][colorIndex] = 1

            for neighbor in adj[node]:
                if dfs(neighbor) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max (
                        count[node][c], 
                        (1 if c == colorIndex else 0) + count[neighbor][c]
                    )
            path.remove(node)
            return max (count[node])
        
        n , res = len(colors), 0
        visit, path = set(), set()
        count = [[0]* 26 for i in range(n)]
        for i in range(n):
            val = dfs(i)
            if val == float("inf"):
                return -1
            res = max(val, res)
        return res
