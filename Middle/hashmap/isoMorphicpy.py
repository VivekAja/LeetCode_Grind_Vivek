from collections import Counter
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}
        s1 = Counter(s)
        print(s1)
        for ch_s, ch_t in zip(s, t):
            #print(ch_s, ch_t)
            if ch_s in s_to_t:
                if s_to_t[ch_s] != ch_t:
                    return False
            else:
                if ch_t in t_to_s:  # avoid two-to-one mapping
                    #print('two',ch_s, ch_t)
                    return False
                s_to_t[ch_s] = ch_t
                t_to_s[ch_t] = ch_s

        return True
if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("badc", "baba"))  # True
    print(s.isIsomorphic("foo", "bar"))  # False
    print(s.isIsomorphic("paper", "title"))  # True
    print(s.isIsomorphic("ab", "aa"))  # False