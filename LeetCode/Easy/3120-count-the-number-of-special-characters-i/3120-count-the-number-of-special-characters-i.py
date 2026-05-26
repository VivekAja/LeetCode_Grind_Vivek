from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #char_counts = Counter(word)
        char = set(word)
        count = 0
        for i in range(26):
            lower = chr(97+i)
            upper = chr(65+i)

            if lower in char and upper in char:
                count +=1
        return count