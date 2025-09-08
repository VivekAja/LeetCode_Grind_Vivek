class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(n ,0 ,-1):
            b = n - a
            string = str(a) + str(b)
            if '0' not in string:
                return [a, b]
