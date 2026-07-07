class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x =""
        y = 0
        if n <=0:
            return 0
        for i in str(n):
            z = int(i)
            if z!=0:
                x +="".join(i)
                y+=z
        return int(x)* y