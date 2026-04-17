class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):          # enough for 10^9
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1
            or_res = a_bit | b_bit
            if c_bit == 0:
                flips += a_bit + b_bit
            else:
                if a_bit ==0 and b_bit == 0:
                    flips += 1
        return flips
        