class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(0, n, 3):
            sub = nums[i:i+3]
            if len(sub)<3 or sub[2] - sub[0]>k:
                return []
            res.append(sub)
        return res