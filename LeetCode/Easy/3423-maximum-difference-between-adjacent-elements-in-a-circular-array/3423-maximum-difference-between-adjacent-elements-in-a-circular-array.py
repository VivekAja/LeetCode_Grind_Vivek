class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        print(nums)
        maxx = float('-inf')
        for i in range(len(nums)-1):
            sub = abs(nums[i]- nums[i+1])
            maxx = max(sub, maxx)
        return maxx

