class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        summ, count = 0, 0
        minloss =  float('inf')
        for n in nums:
            xor = n^k
            if xor > n:
                count += 1
                summ += xor
            else:
                summ += n
            minloss = min(minloss, abs(n - xor))

        if count%2 == 0:
            return summ
        return summ - minloss
