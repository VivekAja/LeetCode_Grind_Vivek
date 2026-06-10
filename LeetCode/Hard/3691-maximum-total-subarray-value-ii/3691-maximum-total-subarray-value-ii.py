from heapq import heappush, heappop
from typing import List

class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.max_tree = [0] * (4 * self.n)
        self.min_tree = [0] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            # Leaf node — store the element itself
            self.max_tree[node] = data[start]
            self.min_tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child  = 2 * node + 1
            right_child = 2 * node + 2
            self._build(data, left_child,  start, mid)
            self._build(data, right_child, mid + 1, end)
            # Internal node — merge children
            self.max_tree[node] = max(self.max_tree[left_child], self.max_tree[right_child])
            self.min_tree[node] = min(self.min_tree[left_child], self.min_tree[right_child])

    def query_max(self, l, r):
        return self._query_max(0, 0, self.n - 1, l, r)

    def _query_max(self, node, start, end, l, r):
        if r < start or end < l:
            return float('-inf')           # completely outside
        if l <= start and end <= r:
            return self.max_tree[node]     # completely inside
        mid = (start + end) // 2
        left_val  = self._query_max(2 * node + 1, start, mid,     l, r)
        right_val = self._query_max(2 * node + 2, mid + 1, end,   l, r)
        return max(left_val, right_val)

    def query_min(self, l, r):
        return self._query_min(0, 0, self.n - 1, l, r)

    def _query_min(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')            # completely outside
        if l <= start and end <= r:
            return self.min_tree[node]     # completely inside
        mid = (start + end) // 2
        left_val  = self._query_min(2 * node + 1, start, mid,     l, r)
        right_val = self._query_min(2 * node + 2, mid + 1, end,   l, r)
        return min(left_val, right_val)


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SegmentTree(nums)

        # Same heap logic as before — untouched
        pq = []
        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heappush(pq, (-val, l, n - 1))

        ans = 0
        for _ in range(k):
            val, l, r = heappop(pq)
            ans += -val
            if r > l:
                val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heappush(pq, (-val, l, r - 1))

        return ans