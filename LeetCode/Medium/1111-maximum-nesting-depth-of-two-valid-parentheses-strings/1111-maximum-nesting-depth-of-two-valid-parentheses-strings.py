class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """
        bal = -1
        start = False
        res = []
        for s in seq:
            if s == "(":
                bal += 1
                start = True
                res.append(bal)

            elif s == ")" and start:
                bal -= 1
                
        op = []
        cl = []
        i = 0
        while i < len(seq):
            if seq[i] == "(":
                if op:
                    opval = len(op) -1 
                    op.append(opval)
                else:
                    res.append(0)
            else:
                if op:
                    val = op.pop()

        """
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



            