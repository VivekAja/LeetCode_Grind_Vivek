class Solution:
    def passwordStrength(self, password: str) -> int:
        lower = set("abcdefghijklmnopqrstuvwxyz")
        upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        nums = set("0123456789")
        sp = set("!@#$")
        out = 0
        b = set()
        for x in password:
            if x not in b:
                b.add(x)
        for p in b:
            if p in lower:
                out+=1
            elif p in upper:
                out+=2
            elif p in nums:
                out+=3
            else:
                out+=5
        return out
