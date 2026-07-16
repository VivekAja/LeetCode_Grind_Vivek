class Solution:
    def gcd(a, b):
        while b:
            a, b = b, a%b
            return a
    def gcdSum(self, nums: list[int]) -> int:
        prefixedGCD = [0] * len(nums)
        count = 0
        cur = float('-inf')
        for i in range(len(nums)):
            cur = max(cur, nums[i])
            prefixedGCD[i] = gcd(cur, nums[i])
        prefixedGCD.sort()
        left = 0
        right = len(prefixedGCD) -1
        while left < right:
            count += gcd(prefixedGCD[left], prefixedGCD[right])
            left +=1
            right -=1
        return count
