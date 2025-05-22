class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        directed = set()

        # Build the undirected graph and store original direction
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            directed.add((u, v))  # edge is directed from u to v

        visited = set()
        changes = 0

        def dfs(city):
            nonlocal changes
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    # If the original edge was from city to neighbor, it needs to be reversed
                    if (city, neighbor) in directed:
                        changes += 1
                    dfs(neighbor)

        dfs(0)
        return changes