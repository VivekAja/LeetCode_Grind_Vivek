class Solution:
    def isvalid(self, nums, m , p):
        i, pairs = 0, 0
        while i<len(nums)-1:
            if nums[i+1]-nums[i] <= m:
                pairs += 1
                i += 2
            else:
                i += 1
        return pairs>=p

    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = nums[n-1] - nums[0]
        result = float('inf')
        if p == 0:
            return 0

        while left<=right:
            m = left + (right-left)//2
            if (self.isvalid(nums, m, p)):
                result = m
                right = m-1
            else:
                left = m+1
        return int(result)

