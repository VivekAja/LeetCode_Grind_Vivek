class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour < 12:
            h = hour * 30 + minutes * 0.5
        else:
            h = minutes* 0.5
        m = minutes * 6
        print(h, m, h-m)
        if abs(h-m) > 180:
            return 360 - float(abs(h-m))
        else:
            return float(abs(h-m))