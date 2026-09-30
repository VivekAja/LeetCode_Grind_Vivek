class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = [0] * len(seq)
        depth = 0

        for i, ch in enumerate(seq):
            if ch == "(":
                res[i] = depth & 1
                depth += 1
            else:
                depth -= 1
                res[i] = depth & 1
        return res



            