class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur = 0
                count = max(count, cur)
                
            else:
                cur+=1
                #count+=1
                count = max(count, cur)
        return count 