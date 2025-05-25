class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(i:int, rem: int):
            if rem == 0 and len(combi) == k:
                result.append(combi[:])
                return
            if i > 9 or i > rem or len(combi) >= k:
                return
            combi.append(i)
            dfs(i+1, rem - i)
            combi.pop()
            dfs(i+1, rem)
        combi = []
        result = []
        dfs(1, n)
        return result