class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        res = []
        for i in range(n):
            if i == 0 or groups[i] != groups[i-1]:
                res.append(words[i])

        return res