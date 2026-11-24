class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map.get(key, [])
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid][0] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        return lst[lo-1][1] if lo else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)