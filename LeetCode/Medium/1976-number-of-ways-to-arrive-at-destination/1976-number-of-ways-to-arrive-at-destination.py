class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, weight in roads:
            adj[src].append((weight, dst))
            adj[dst].append((weight, src))

        MOD = 10**9+7
        minheap = [(0,0)] #cost, node
        mincost = [float('inf')] *n
        pathcount = [0]*n
        pathcount[0] = 1

        while minheap:
            cost , node = heappop(minheap)

            for neicost, nei in adj[node]:
                if cost + neicost < mincost[nei]:
                    mincost[nei] = cost + neicost
                    pathcount[nei]= pathcount[node]
                    heappush(minheap,(cost+neicost, nei))
                elif cost+neicost == mincost[nei]:
                    pathcount[nei] = (pathcount[node]+pathcount[nei]) % MOD
        return pathcount[n-1]


