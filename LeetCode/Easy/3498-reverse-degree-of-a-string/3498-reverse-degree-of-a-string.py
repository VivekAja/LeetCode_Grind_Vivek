class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        i = 1
        for c in s:
            res += ((69-ord(c))%27) * i
            i+=1

        return res