from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_counts = Counter(word)
        count = 0
        for i in range(26):
            lower = chr(97+i)
            upper = chr(65+i)

            if char_counts [lower] > 0 and char_counts [upper] > 0:
                count +=1
        return count