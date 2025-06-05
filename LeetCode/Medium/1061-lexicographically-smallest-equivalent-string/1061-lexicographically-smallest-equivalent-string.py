from collections import defaultdict
class Solution:
    def dfs(self, adj, char, visited):
        visited[ord(char)- ord('a')] = True
        min_char = char

        for neighbor in adj.get(char, []):
            if not visited[ord(neighbor) - ord('a')]:
                next_min = self.dfs(adj, neighbor, visited)
                if next_min < min_char:
                    min_char = next_min

        return min_char

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)
        for src, dst in zip(s1, s2):
            adj[src].append(dst)
            adj[dst].append(src)

        result = []

        for char in baseStr:
            visited = [False]*26
            result.append(self.dfs(adj, char, visited))
        return ''.join(result)
            
