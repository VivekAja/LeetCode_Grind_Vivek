from collections import deque
from typing import List

class Solution:
    def bfs(self, start: int, adj: List[List[int]], included: List[bool] = None) -> int:
        q = deque()
        q.append((start, -1))
        count = 0
        level = 0

        while q:
            size = len(q)
            if level % 2 == 0:
                count += size  # count nodes on even levels

            for _ in range(size):
                curr, parent = q.popleft()
                if included is not None and level % 2 == 0:
                    included[curr] = True
                for neighbor in adj[curr]:
                    if neighbor == parent:
                        continue
                    q.append((neighbor, curr))
            level += 1

        return count

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        # Build adjacency lists
        adj1 = [[] for _ in range(n1 + 1)]
        adj2 = [[] for _ in range(n2 + 1)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Step 1: Get best possible nodes in tree-2
        even_count2 = self.bfs(0, adj2)
        odd_count2 = n2 - even_count2
        best2 = max(even_count2, odd_count2)

        # Step 2: Mark even-level nodes in tree-1
        included = [False] * n1
        even_count1 = self.bfs(0, adj1, included)

        # Step 3: Build answer array
        ans = [0] * n1
        for i in range(n1):
            if included[i]:
                ans[i] = even_count1 + best2
            else:
                ans[i] = (n1 - even_count1) + best2

        return ans