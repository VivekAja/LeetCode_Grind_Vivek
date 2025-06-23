class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            nn = sorted(stones)
            if len(nn)>2:
                first = nn[-1]
                sec = nn[-2]
            elif len(nn) == 2:
                return abs(nn[0] - nn[1])
            elif len(nn) == 1:
                return nn[0]
            stones.remove(first)
            stones.remove(sec)
            n = abs(sec - first)
            stones.append(n)
        return stones