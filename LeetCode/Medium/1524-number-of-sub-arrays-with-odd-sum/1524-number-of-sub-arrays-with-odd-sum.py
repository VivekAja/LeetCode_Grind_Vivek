class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 0
        MOD = (10**9+7)
        answer = 0
        for num in arr:
            if num%2==0:
                new_odd = odd
                new_even = even + 1
            else:
                new_odd = even + 1
                new_even = odd

            odd = new_odd
            even = new_even

            answer = (answer + odd) % MOD

        return answer