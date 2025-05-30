class Solution:
    def dfs(self, edges: List[int], node:int, dist: List[int], visited: [bool]) -> None:
        visited[node] = True
        neighbor = edges[node]
        if neighbor != -1 and not visited[neighbor]:
            dist[neighbor] = dist[node] + 1
            self.dfs(edges, neighbor, dist, visited)

    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf')]*n
        dist2 = [float('inf')]*n

        visited1 = [False] * n
        visited2 = [False] * n

        dist1[node1] = 0
        dist2[node2] = 0

        self.dfs(edges, node1, dist1, visited1)
        self.dfs(edges, node2, dist2, visited2)

        min_node = -1
        min_dist = float('inf')

        for i in range(n):
            if dist1[i] != float('inf') and dist2[i] != float('inf'):
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    min_node = i

        return min_node
