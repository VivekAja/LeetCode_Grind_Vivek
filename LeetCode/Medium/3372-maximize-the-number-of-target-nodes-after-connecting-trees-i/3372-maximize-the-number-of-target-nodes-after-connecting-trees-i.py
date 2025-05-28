from collections import defaultdict, deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # BFS to find all the nodes within Tree1 within k distance
        def bfs_all_nodes_within_k(edges, k):
            adj = defaultdict(list)
            n = max(max(u, v) for u, v in edges) + 1 
            result = []

            for src, dst in edges:
                adj[src].append(dst)
                adj[dst].append(src)

            for start in range(n):
                visited = [False] * n
                queue = deque([(start, 0)])
                visited[start] = True
                count = 0  # Including the node itself

                while queue:
                    node, dist = queue.popleft()
                    if dist > k:
                        continue
                    count += 1

                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append((neighbor, dist + 1))

                result.append((start, count))
            return result

        # Run BFS on both trees
        result1 = bfs_all_nodes_within_k(edges1, k)
        result2 = bfs_all_nodes_within_k(edges2, k-1)

        # Find max count in second tree
        max_count_res2 = max(count for _, count in result2)

        # Add max from res2 to all in res1
        final = [count + max_count_res2 for _, count in result1]

        return final