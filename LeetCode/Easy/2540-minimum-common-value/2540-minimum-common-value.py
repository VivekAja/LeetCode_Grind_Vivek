class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        1. Hashmap Approach
        set1 = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in set1:
                return nums1[i]
        return -1
        TC: O(N+M)
        SC: O(1)
        ================
        2. Binary Search 
        """
        def binarys(arr, target):
            l, r  = 0, len(arr)-1
            while l<=r:
                mid = (l+r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid+1
                else:
                    #nums[mid] > target:
                    r = mid -1
            return False
        for num in nums1:
            if binarys(nums2, num):
                return num
        return -1



