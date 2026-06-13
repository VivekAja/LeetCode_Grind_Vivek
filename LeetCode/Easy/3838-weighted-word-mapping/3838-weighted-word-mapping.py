class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        val =0
        sett = set('abcdefghijklmnopqrstuvwxyz')
        sett= sorted(list(sett))
        for word in words:
            for w in word:
                n = ord(w) - ord('a')
                
                val += weights[n]

                #print(val)
            fin = val % 26
            res+= "".join(sett[25-fin])
            val, fin =0, 0
        return res
