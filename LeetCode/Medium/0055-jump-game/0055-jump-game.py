class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        reach = 0
        for i in range(n):
            if i> reach:
                return False
            reach = max(reach, i+nums[i])

            if reach >= n-1:
                return True
        return False



        