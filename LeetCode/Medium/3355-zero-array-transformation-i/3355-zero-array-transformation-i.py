class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        
        for i in range(len(queries)):
            start = queries[i][0]
            end  = queries[i][1]

            while start<=end:
                if nums[start]!=0:
                    nums[start] -= 1
                start += 1

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                return False
        return True
        """
        n = len(nums)
        diff = [0] * (n+1)

        for start, end in queries:
            diff[start] += 1
            if end+1 < len(diff):
                diff[end+1] -= 1
        rsum = 0
        for i in range(n):
            rsum += diff[i]
            print(rsum)
            if nums[i] > rsum:
                return False
        return True