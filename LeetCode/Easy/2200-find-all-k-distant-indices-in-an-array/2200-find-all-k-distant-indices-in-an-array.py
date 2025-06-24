class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keyin = []
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                keyin.append(i)
        for i in range(len(nums)):
            for j in range(len(keyin)):
                if abs(i-keyin[j]) <= k:
                    res.append(i)
                    break
        return res

        