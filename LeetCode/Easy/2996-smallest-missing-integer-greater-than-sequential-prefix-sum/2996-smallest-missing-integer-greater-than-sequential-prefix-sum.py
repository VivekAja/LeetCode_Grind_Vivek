class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_sum += nums[i]
            else:
                break
        
        nums_set = set(nums)
        while current_sum in nums_set:
            current_sum += 1
            
        return current_sum

