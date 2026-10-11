class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = []
        for i,j in zip(nums1, nums2):
            diff.append(abs(i - j))

        k = k1+k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse = True)
        diff.append(0)

        for i in range(len(diff)-1):
            count = i+1
            gap = diff[i] - diff[i+1]
            cost = count * gap

            if k >= cost:
                k -= cost
            else:
                level, rem = divmod(k, count)

                for j in range(count):
                    diff[j] = diff[i] - level
                    if j < rem:
                        diff[j] -= 1
                k = 0
                break
        return sum(d * d for d in diff)

