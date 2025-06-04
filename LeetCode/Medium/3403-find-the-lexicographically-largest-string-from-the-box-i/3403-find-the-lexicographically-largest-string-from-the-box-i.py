class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        longest = n - (numFriends - 1)
        res = ""
        for i in range(n):
            k = min(longest, n-i)
            res = max(res, word[i:i+k])
        return res