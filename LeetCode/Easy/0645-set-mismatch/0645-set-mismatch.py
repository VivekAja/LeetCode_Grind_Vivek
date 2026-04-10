class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        duplicates = -1
        missing = -1

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for i in range(1, n+1):
            if i in count:
                if count[i] == 2:
                    duplicates  = i
            else:
                missing = i
        return [duplicates, missing]