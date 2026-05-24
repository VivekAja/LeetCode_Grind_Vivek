class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n
        maxi = 0

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            maxi = 1
            
            
            for j in range(i-1,max(-1, i-d-1), -1):
                if arr[j] >= arr[i]:
                    break
                maxi = max(maxi, 1+dfs(j))
            for j in range(i+1,min(n, i+d+1)):
                if arr[j] >= arr[i]:
                    break
                maxi = max(maxi, 1+dfs(j))
            dp[i] = maxi
            return dp[i]
        return max(dfs(i) for i in range(n))