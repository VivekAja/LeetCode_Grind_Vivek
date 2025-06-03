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