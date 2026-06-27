class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)

        maxi = freq[1] - (freq[1] % 2^1)

        del freq[1]

        for num in nums:
            cur_length = 0
            cur = num
            while freq[cur] > 1:
                cur = cur*cur
                cur_length+=2
            if freq[cur]:
                cur_length+=1
            else:
                cur_length-=1 
            maxi = max(maxi, cur_length)
        return maxi
