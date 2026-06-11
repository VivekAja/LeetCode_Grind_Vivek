class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        from collections import deque


        MOD = 10**9 + 7
        
        if not edges:
            return 1 
        
        
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        depth = [-1] * (n + 1)
        depth[1] = 0
        queue = deque([1])
        max_depth = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if depth[neighbor] == -1:
                    depth[neighbor] = depth[node] + 1
                    max_depth = max(max_depth, depth[neighbor])
                    queue.append(neighbor)
        
        return pow(2, max_depth - 1, MOD)

