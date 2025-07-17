class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Initialize a 2D dp array of size k x n, filled with 1s
        dp = [[1] * n for _ in range(k)]

        maxSub = 1

        for i in range(1, n):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                dp[mod][i] = max(dp[mod][i], 1 + dp[mod][j])
                maxSub = max(maxSub, dp[mod][i])

        return maxSub