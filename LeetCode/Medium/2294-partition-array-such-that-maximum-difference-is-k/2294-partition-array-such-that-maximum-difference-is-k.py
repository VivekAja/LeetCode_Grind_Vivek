class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        minval = nums[0]
        count = 1
        for i in range(n):
            if nums[i] - minval > k:
                count += 1
                minval = nums[i]
        return count
