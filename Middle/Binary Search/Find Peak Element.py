class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        left, right = 1, n - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    print(Solution().findPeakElement(nums))
    nums = [1,2,1,3,5,6,4]
    print(Solution().findPeakElement(nums))
    nums = [2,1]
    print(Solution().findPeakElement(nums))