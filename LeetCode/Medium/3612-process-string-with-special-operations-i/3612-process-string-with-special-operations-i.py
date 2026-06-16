class Solution:
    def processStr(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            if ord(s[i]) >=97 and ord(s[i]) <=122:
                res+=s[i]
            if s[i] == '*':
                print(res)
                if len(res) < 1:
                    continue
                else:
                    res= res[:-1]
            if s[i] == '#':
                if len(res) < 1:
                    continue
                else:
                    res+=res

            if s[i] == '%':
                print(res)
                res = res[::-1]

        return res