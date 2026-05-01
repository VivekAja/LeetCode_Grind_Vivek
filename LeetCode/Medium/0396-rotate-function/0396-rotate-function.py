class Solution:
    """
    Brute Force
    def solve(self, rotated):
        cur = 0
        for i in range(len(rotated)):
            cur += (i* rotated[i])
            #print(cur)
        return cur
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        calc = 0
        for i in range(len(nums)):
            rotated = nums[-i:] + nums[:-i]
            #print(rotated)
            cur = self.solve(rotated)
            #print(cur)
            calc = max(cur, calc)
        return calc
        """
    def maxRotateFunction(self, nums: List[int]) -> int:

        fof0 = sum (i* nums[i] for i in range(len(nums)))
        maxf = fof0
        t = sum(nums)

        for i in range(1, len(nums)):
            fof = fof0 + t - (len(nums) * nums[len(nums)-i])
            maxf = max(fof, maxf)
            fof0 = fof 
        return maxf


        