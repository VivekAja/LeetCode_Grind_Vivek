class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi = 0
        
        new_list = [item for item in nums if item > 0]
        print(new_list)
        if len(nums) == 1:
            return sum(nums)
        if not new_list:
            return max(nums)
        seen = set()
        for n in new_list:
            if n in seen:
                continue
            seen.add(n)
            maxi += n 
        return maxi