class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in set1:
                return nums1[i]
        return -1
