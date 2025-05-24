class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        stack = []

        for n in nums2:
            while stack and stack[-1]<n:
                mapp[stack.pop()] = n
            stack.append(n)

        return [mapp.get(n, -1) for n in nums1]