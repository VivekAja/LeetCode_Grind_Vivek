class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        rank = 0
        nsa = sorted(arr)
        for i in nsa:
            if i not in d:
                rank+=1
            d[i] = rank
        return [d[key] for key in arr if key in d]