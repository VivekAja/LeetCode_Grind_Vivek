class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges)+1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary Lifting for LCA
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        def dfs(u, p, d):
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                up[u][i] = up[up[u][i-1]][i-1]
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
                    
        dfs(1, 1, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]: u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v: return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u, v = up[u][i], up[v][i]
            return up[u][0]
        
        MOD = 10**9 + 7
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            # Number of ways is 2^(dist-1)
            results.append(pow(2, dist - 1, MOD))
            
        return results