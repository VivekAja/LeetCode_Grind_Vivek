class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return [0]
        lnums = [0] + nums[:-1]
        rnums = nums[1:] + [0]
        for i in range(1,len(lnums)):
            lnums[i] += lnums[i-1]
        for j in range(len(rnums)-2):
            rnums[j] = sum(rnums[j:])
        res = []
        for i, j in zip(lnums, rnums):
            res.append(abs(i-j))
        return res
