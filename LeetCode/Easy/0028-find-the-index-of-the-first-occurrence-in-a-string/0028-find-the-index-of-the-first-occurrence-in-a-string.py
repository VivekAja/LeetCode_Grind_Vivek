class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n= len(needle)
        print(n)
        for i in range(len(haystack)):
            win = haystack[i:i+n]
            print(win)
            if needle == win:
                return i
        return -1