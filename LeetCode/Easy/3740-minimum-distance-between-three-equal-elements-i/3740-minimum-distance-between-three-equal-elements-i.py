class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maps = defaultdict(list)
        result = float('inf')

        for k in range(n):
            maps[nums[k]].append(k)
            if len(maps[nums[k]]) >= 3:
                vec = maps[nums[k]]
                siz = len(vec)
                i = vec[siz - 3]
                result = min(result, k - i)

        return -1 if result == float('inf') else 2 * result