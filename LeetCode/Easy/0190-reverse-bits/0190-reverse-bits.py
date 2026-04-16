class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for pos in range(32):
            bit = (n >> pos) & 1
            if bit:
                result |= (1 << (31 - pos)) 
        return result
        