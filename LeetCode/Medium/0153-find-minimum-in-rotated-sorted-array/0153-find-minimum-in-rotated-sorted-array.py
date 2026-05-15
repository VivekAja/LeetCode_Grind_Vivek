import heapq
class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = []
        for num in nums:
            heapq.heappush(mini, num)
        return heapq.heappop(mini)