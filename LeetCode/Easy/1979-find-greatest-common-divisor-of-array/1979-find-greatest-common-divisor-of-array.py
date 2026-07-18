class Solution:
    def gcd(a,b):
        a,b = b, a%b
        return a
    def findGCD(self, nums: List[int]) -> int:
        x = max(nums)
        y = min(nums)
        return gcd(x, y)