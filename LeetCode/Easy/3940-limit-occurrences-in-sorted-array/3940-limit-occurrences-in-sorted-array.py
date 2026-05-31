from collections import Counter
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        idx = 0
        for num in nums:
            cur_count = counts.get(num, 0)
            if cur_count < k:
                nums[idx] = num
                counts[num] = cur_count+1
                idx +=1
        return nums[:idx]        
