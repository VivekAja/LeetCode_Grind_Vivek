from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        result = 0

        for word in words:
            rev = word[::-1]
            if count[rev] > 0:
                result += 4
                count[rev] -= 1
            else:
                count[word] += 1

        for word, freq in count.items():
            print(freq)
            if word[0] == word[1] and freq > 0:
                result += 2
                break
        return result