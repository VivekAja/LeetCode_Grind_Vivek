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
    def __init__(self, nums1, nums2):
        self.vec1 = nums1
        self.vec2 = nums2
        self.mp = Counter(nums2)

    def add(self, index, val):
        old_val = self.vec2[index]
        self.mp[old_val] -= 1
        if self.mp[old_val] == 0:
            del self.mp[old_val]  # Clean up
        self.vec2[index] += val
        self.mp[self.vec2[index]] += 1

    def count(self, tot):
        count = 0
        for x in self.vec1:
            count += self.mp[tot - x]
        return count