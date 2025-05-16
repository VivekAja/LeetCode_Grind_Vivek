class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        def hummingDistance (s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff+=1
                elif diff > 1:
                    return False
            return diff == 1

        n = len(words)
        result = []
        dp = [1] * n
        parent = [-1] * n
        longestSub = 1
        longestSubIdx = 0

        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] and len(words[i]) == len(words[j]) and hummingDistance(words[i], words[j]):
                    if (dp[j] + 1 > dp[i]):
                        dp[i] = dp[j] + 1
                        parent[i] = j

                        if (longestSub < dp[i]):
                            longestSub = dp[i]
                            longestSubIdx = i
        while (longestSubIdx != -1):
            result.append(words[longestSubIdx])
            longestSubIdx = parent[longestSubIdx]
        #result = reversed(result)
        return result[::-1]
        