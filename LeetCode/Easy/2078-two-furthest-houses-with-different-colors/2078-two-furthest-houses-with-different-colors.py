class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        maxi = 0
        for i in range(n):
            for j in range(n-1, -1, -1):
                if colors[i]!= colors[j]:
                    cur = abs(i - j)
                    maxi = max(cur, maxi)
        print(maxi)
        return maxi
        