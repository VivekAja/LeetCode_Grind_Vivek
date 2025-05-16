from collections import defaultdict


class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        ans = float('inf')
        n = len(tops)

        freq = defaultdict(int)
        for i in range(n):
            freq[tops[i]] += 1
            if bottoms[i] != tops[i]:
                freq[bottoms[i]] += 1
        print(freq, n, freq[tops[0]], freq[bottoms[0]])
        for i in range(1, 7):
            if freq[i] < n:
                continue
            count_top = 0
            count_bottom = 0
            for j in range(n):
                if tops[j] != i:
                    count_top += 1
                if bottoms[j] != i:
                    count_bottom += 1

            ans = min(ans, min(count_top, count_bottom))

        return -1 if ans == float('inf') else ans
if __name__ == '__main__':
    tops = [1, 2, 1, 1, 1, 2, 2, 2]
    bottoms = [2, 1, 2, 2, 2, 2, 2, 2]
    print(Solution().minDominoRotations(tops, bottoms))  # Output: 2
    tops = [3,5,1,2,3]
    bottoms = [3,6,3,3,4]
    print(Solution().minDominoRotations(tops, bottoms))  # Output: -1