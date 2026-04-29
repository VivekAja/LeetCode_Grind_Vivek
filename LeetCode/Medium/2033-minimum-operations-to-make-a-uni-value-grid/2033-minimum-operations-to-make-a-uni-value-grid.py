class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [num for i in grid for num in i]
        flat.sort()
        median = flat[len(flat)// 2]
        count = 0
        if len(flat) < 2:
            return 0
        for num in flat:
            if abs(num - median) %x != 0:
                return -1
            count += abs(num - median) // x                    
        return count

