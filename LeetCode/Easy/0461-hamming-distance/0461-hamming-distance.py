class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            if (1<<i) & x != (1<<i)& y:
                count+=1
        return count
        