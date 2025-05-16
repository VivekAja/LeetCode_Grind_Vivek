class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            print(mid, hours)
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed(piles = [3,6,7,11], h = 8))