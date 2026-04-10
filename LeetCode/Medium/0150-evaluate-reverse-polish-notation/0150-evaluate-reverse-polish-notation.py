class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        set = {"+","-","*","/"}
        if len(tokens)<2:
            return int(tokens[0])
        for i in tokens:
            if i not in set:
                res.append(i)
            else:
                if i == "+":
                    sec = res.pop()
                    fir = res.pop()
                    result = int(fir) + int(sec)
                    res.append(result)
                if i == "-":
                    sec = res.pop()
                    fir = res.pop()
                    result = int(fir) - int(sec)
                    res.append(result)
                if i == "*":
                    sec = res.pop()
                    fir = res.pop()
                    result = int(fir)* int(sec)
                    res.append(result)         
                if i == "/":
                    sec = res.pop()
                    fir = res.pop()
                    result = int(fir)/int(sec)
                    res.append(int(result))
        return res[0]