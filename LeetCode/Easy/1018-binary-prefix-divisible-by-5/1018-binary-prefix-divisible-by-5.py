class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        x = 0
        for a in nums:
            x = (x << 1 | a) % 5
            result.append(x == 0)
        return result