import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n < 0:
            return -1

        r = (n)*(n+1)//2
        x = math.isqrt(r)
        if x*x == r:
            return x
        return -1