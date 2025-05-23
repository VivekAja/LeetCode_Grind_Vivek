#BFS

#Time Complexity: O(n²)
#Space Complexity: O(n)

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


============================================================================
#BFS

#Time Complexity: O(n²)
#Space Complexity: O(n)



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            while queue:
                fromnode = queue.popleft()
                print(fromnode)
                for tonode in range(n):
                    if isConnected[fromnode][tonode] and tonode not in visited:
                        visited.add(tonode)
                        queue.append(tonode)

        for i in range(n):
            if i not in visited:
                bfs(i)
                provinces += 1
        return provinces
        
