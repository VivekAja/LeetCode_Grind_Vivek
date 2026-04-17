class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        maxlen = max(len(x_bin), len(y_bin))
        sx = x_bin.zfill(maxlen)
        sy = y_bin.zfill(maxlen)
        count = 0
        for a, b in zip(sx, sy):
            if a!= b:
                count+=1
        return count
        