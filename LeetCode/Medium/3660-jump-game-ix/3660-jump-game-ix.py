class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0: return []

        # Step 1: Precompute prefix maximums
        # pre_max[i] is the maximum value from index 0 to i
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], nums[i])

        # Step 2: Precompute suffix minimums
        # suf_min[i] is the minimum value from index i to n-1
        suf_min = [0] * n
        suf_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suf_min[i] = min(suf_min[i+1], nums[i])

        ans = [0] * n
        start = 0
        # Step 3: Identify components and fill the answer
        for i in range(n):
            # A cut exists at i if max(left) <= min(right)
            # or if we've reached the end of the array
            if i == n - 1 or pre_max[i] <= suf_min[i+1]:
                # The max value reachable in this component is pre_max[i]
                component_max = pre_max[i]
                for k in range(start, i + 1):
                    ans[k] = component_max
                start = i + 1
        return ans