class Solution:
    def isGood(self, nums: List[int]) -> bool:
        gud = sorted(nums)
        n = len(nums)
        if n-1 != gud[-1]:
            print(gud[-1])
            return False
        print(gud)
        for i, j in enumerate(gud):
            print(i, j)
            if i+1 != j and i<n-1:
                print("l")
                return False
        return True