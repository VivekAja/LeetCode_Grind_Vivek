class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        soort = sorted(count.items(), reverse = True)

        for n, f in soort:
            if n == f:
                return n
        return -1