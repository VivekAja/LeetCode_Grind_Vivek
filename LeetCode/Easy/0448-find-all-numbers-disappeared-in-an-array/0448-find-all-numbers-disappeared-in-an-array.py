class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rank = {}
        for val in nums:
            rank[val] = True
        return [i for i in range(1, len(nums)+1) if i not in rank]