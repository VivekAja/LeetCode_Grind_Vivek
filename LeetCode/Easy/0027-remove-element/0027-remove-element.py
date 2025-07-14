class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0

        for num in nums:
            if num!= val:
                nums[n] = num
                n+=1
        return n