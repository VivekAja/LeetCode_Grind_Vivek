class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        l = 1
        for i in range(n):
            ans[i] = l
            l *= nums[i]
        
        r = 1
        for i in reversed(range(n)):
            ans[i] *= r
            r *= nums[i]
        return ans