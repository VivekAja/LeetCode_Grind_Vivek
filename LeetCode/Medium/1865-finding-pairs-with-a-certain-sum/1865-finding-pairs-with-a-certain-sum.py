class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.counts[old] -=1
        if self.counts[old] == 0:
            del self.counts[old]
        self.nums2[index] += val
        self.counts[self.nums2[index]] +=1

        

    def count(self, tot: int) -> int:
        res = 0
        for value in self.nums1:
            res += self.counts[tot - value]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
