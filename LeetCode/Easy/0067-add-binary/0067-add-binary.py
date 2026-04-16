class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = 0
        n = 0
        for i in range(len(a)):
            n += int(a[i]) * (2 ** (len(a) - 1 - i))
        for j in range(len(b)):
            m += int(b[j]) * (2 ** (len(b) - 1 - j))
        v = m + n
        v = f"{v:b}"
        return v