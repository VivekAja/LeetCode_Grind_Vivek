class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        L = 0
        length_history = []


        for i in range(n):
            length_history.append(L)
            ch = s[i]
            if ch == '*':
                if L > 0:
                    L -= 1
            elif ch == '#':
                L *= 2
            elif ch == '%':
                continue
            else:  # 'a' to 'z'
                L += 1

        if k >= L or k < 0:
            return '.'

        # Backward pass
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_L = length_history.pop()

            if ch == '%':
                k = L - k - 1
            elif ch == '#':
                if k >= prev_L:
                    k -= prev_L
            
            L = prev_L

            if 'a' <= ch <= 'z' and k == L:
                return ch

        return '.'