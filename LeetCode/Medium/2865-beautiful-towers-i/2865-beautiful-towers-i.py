class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        maxx = 0
        n = len(heights)
        for i in range(n):
            current = heights[i]
            total = current

            minh = current
            for j in range(i-1,-1,-1):
                minh = min(minh, heights[j])
                total += minh
                    
                    
            minh = current
            for j in range(i+1,n):
                minh = min(minh, heights[j])
                total += minh

            maxx = max(total, maxx)

        return maxx