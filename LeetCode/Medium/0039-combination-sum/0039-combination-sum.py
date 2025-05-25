class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, cursum: int):
            if cursum == 0:
                combinations.append(combisofar[:])
            if i >= len(candidates) or cursum < candidates[i]:
                return
            dfs(i+1, cursum)
            combisofar.append(candidates[i])
            dfs(i, cursum - candidates[i])
            combisofar.pop()
        candidates.sort()
        combisofar = []
        combinations = []
        dfs(0, target)
        return combinations