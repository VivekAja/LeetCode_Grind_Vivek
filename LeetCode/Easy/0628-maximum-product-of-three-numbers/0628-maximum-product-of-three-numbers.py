class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        """
        if nums[0]* nums[1] > nums[-1]:
            return nums[0]* nums[1] * nums[-1]
        else:
            return nums[-3] * nums[-2] * nums[-1]
            """
        pos = nums[-3] * nums[-2] * nums[-1]
        neg = nums[0]* nums[1] * nums[-1]
        if pos > neg:
            return pos
        else:
            return neg
        
