class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        temp = offset = 0
        prev_index = len_s = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                temp += 1 << offset
                if temp > k:
                    return s[:prev_index].count('0') + len_s - prev_index
                prev_index = i
            offset += 1
        return len_s