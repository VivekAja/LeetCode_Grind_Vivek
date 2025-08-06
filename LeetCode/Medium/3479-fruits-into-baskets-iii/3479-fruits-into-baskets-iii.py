class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        segment_tree = [0] * (4 * n)

        # Build segment tree
        self._build(0, 0, n - 1, baskets, segment_tree)

        unplaced = 0
        for fruit in fruits:
            if not self._query_segment_tree(0, 0, n - 1, segment_tree, fruit):
                unplaced += 1

        return unplaced

    def _build(self, i: int, l: int, r: int, baskets: list[int], segment_tree: list[int]) -> None:
        if l == r:
            segment_tree[i] = baskets[l]
            return

        m = (l + r) // 2
        self._build(2 * i + 1, l, m, baskets, segment_tree)
        self._build(2 * i + 2, m + 1, r, baskets, segment_tree)
        segment_tree[i] = max(segment_tree[2 * i + 1], segment_tree[2 * i + 2])

    def _query_segment_tree(self, i: int, l: int, r: int, segment_tree: list[int], val: int) -> bool:
        if segment_tree[i] < val:
            return False  # No basket in this segment

        if l == r:
            segment_tree[i] = -1  # Mark basket as used
            return True

        mid = (l + r) // 2
        if segment_tree[2 * i + 1] >= val:
            placed = self._query_segment_tree(2 * i + 1, l, mid, segment_tree, val)
        else:
            placed = self._query_segment_tree(2 * i + 2, mid + 1, r, segment_tree, val)

        segment_tree[i] = max(segment_tree[2 * i + 1], segment_tree[2 * i + 2])
        return placed