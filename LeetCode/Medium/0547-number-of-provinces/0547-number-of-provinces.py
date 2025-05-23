class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set()
        provinces = 0

        for city in range(len(isConnected)):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces