class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            swapped = False

        # Last i elements are already in place
            for j in range(0, n-i-1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if (swapped == False):
                break