from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        count = Counter(nums)

        min_heap = []

        for n, freq in count.items():
            heappush(min_heap, (freq, n))

            if len(min_heap) > k:
                heappop(min_heap)
        res = [pair[1] for pair in min_heap]

        return res