class Solution:
    def checkString(self, s: str) -> bool:
        """
        flag = True
        for c in s:
            if c == "b":
                flag = False
            else:
                if not flag:
                    return True
        return not flag
        """
        start = True
        saw = False
        for c in s:
            if c == "b":
                start = True
                saw = True
            else:
                if start and saw:
                    return False
        return start if not saw else saw
