class Solution:
    def __init__(self):
        self.result = ""

    def is_subsequence(self, s: str, sub: str, k: int) -> bool:
        i = j = 0
        n, m = len(s), len(sub)
        while i < n and j < k * m:
            if s[i] == sub[j % m]:
                j += 1
            i += 1
        return j == k * m

    def backtrack(self, s: str, curr: list, can_use: list, freq: list, k: int, max_len: int):
        if len(curr) > max_len:
            return

        candidate = ''.join(curr)
        if (len(candidate) > len(self.result) or
           (len(candidate) == len(self.result) and candidate > self.result)):
            if self.is_subsequence(s, candidate, k):
                self.result = candidate

        for i in reversed(range(26)):  # from 'z' to 'a'
            if not can_use[i] or freq[i] == 0:
                continue
            curr.append(chr(i + ord('a')))
            freq[i] -= 1
            self.backtrack(s, curr, can_use, freq, k, max_len)
            freq[i] += 1
            curr.pop()

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter

        freq_total = Counter(s)
        freq = [0] * 26
        can_use = [False] * 26

        for c in range(26):
            if freq_total[chr(c + ord('a'))] >= k:
                can_use[c] = True
                freq[c] = freq_total[chr(c + ord('a'))] // k

        max_len = len(s) // k
        self.backtrack(s, [], can_use, freq, k, max_len)

        return self.result