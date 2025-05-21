#Optimal
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)


=========================================================
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = dict()

        for c in s:
            if c not in seen:
                seen[c] = 0
            seen[c] += 1

        print(seen)

        for c in t:
            if c not in seen:
                return c

            if seen[c] == 0:
                return c

            seen[c] -= 1
