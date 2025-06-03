#Approach-1 (Using DFS)
#T.C : O(n), where n =  number of boxes, we don't visit any box more than once
#S.C : O(n)
class Solution:
    def dfs(self, box: int, status: list[int], candies: list[int], keys: list[list[int]],
            containedBoxes: list[list[int]], visited: set[int], foundBoxes: set[int]) -> int:

        if box in visited:
            return 0

        if status[box] == 0:
            # If the box is closed, we add it to foundBoxes so we can
            # try to open it later if we find its key.
            foundBoxes.add(box)
            return 0

        # Mark the box as visited (meaning we have opened and processed it)
        visited.add(box)
        totalcandies = candies[box]

        # Recursively explore boxes inside the current box
        for insidebox in containedBoxes[box]:
            totalcandies += self.dfs(insidebox, status, candies, keys, containedBoxes, visited, foundBoxes)

        # Process keys found in the current box
        for boxkey in keys[box]:
            status[boxkey] = 1  # Mark the box corresponding to the key as openable

            # If this boxkey was previously found but couldn't be opened,
            # now that we have its key, we can try to open it.
            if boxkey in foundBoxes:
                totalcandies += self.dfs(boxkey, status, candies, keys, containedBoxes, visited, foundBoxes)

        return totalcandies

    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]],
                    containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        
        totalcandies = 0
        visited = set()
        foundBoxes = set() # Renamed 'found' to 'foundBoxes' for clarity and consistency

        # Start DFS from the initial boxes
        for box in initialBoxes:
            totalcandies += self.dfs(box, status, candies, keys, containedBoxes, visited, foundBoxes)
            
        return totalcandies
        found = set()

        for box in initialBoxes:
            totalcandies += self.dfs(box, status, candies, keys, containedBoxes, visited, found)
        return totalcandies



#Approach-2 (Using BFS)
#T.C : O(n), where n =  number of boxes, we don't visit any box more than once
#S.C : O(n)

from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total = 0
        visited = set()
        found = set()
        queue = deque()
        for box in initialBoxes:
            found.add(box)
            if status[box] == 1:
                queue.append(box)
                visited.add(box)
                total += candies[box]

        while queue:
            box = queue.popleft()

            for insidebox in containedBoxes[box]:
                found.add(insidebox)
                if status[insidebox] == 1 and insidebox not in visited:
                    queue.append(insidebox)
                    visited.add(insidebox)
                    total += candies[insidebox]

            for key in keys[box]:
                status[key] = 1
                if key in found and key not in visited:
                    queue.append(key)
                    visited.add(key)
                    total += candies[key]
        return total
