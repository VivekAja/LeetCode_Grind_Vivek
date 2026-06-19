class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur, maxi = 0, 0
        for i in range(len(gain)):
            cur += gain[i]
            maxi = max(maxi, cur)
        return maxi
