class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = sorted(nums)
        if n[0] + n[1] <= n[2]:
            return "none"
        elif n[0] == n[1] == n[2]:
            return "equilateral"
        elif n[0] == n[1] or n[1] == n[2] or n[0] ==n[2]:
            return "isosceles"
        else:
            return "scalene"