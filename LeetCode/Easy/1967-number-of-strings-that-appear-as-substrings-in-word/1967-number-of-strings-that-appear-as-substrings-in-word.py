class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        sett = set(word)
        count = 0
        for word in patterns:
            if len(word)>1:
                for w in word:
                    if w in sett:
                        count+=1
                        break
            else:
                if word in sett:
                    count+=1
        return count 
        """
        count = 0
        for w in patterns:
            if w in word:
                count+=1
        return count