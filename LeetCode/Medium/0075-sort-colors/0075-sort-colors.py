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

========================================================================
#One Pass Solution 
#Constant Space
#DutchNationalFlag
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        low = 0
        mid = 0
        end = len(nums) - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low],nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end],nums[mid]
                end -= 1
