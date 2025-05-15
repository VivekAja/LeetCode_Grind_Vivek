class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        seen = set()
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False