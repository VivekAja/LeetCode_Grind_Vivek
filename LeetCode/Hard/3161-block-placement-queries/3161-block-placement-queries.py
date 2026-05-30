from sortedcontainers import SortedList
class Solution:
    def __init__(self):
        self.size = 500005
        self.seg = [0] * (self.size*4)
    
    def _insert(self, i, val, cur, l, r):
        if l == r:
            self.seg[cur] = val
            return
        mid = (l+r)//2
        if i<=mid:
            self._insert(i, val, cur*2,l,mid)
        else:
            self._insert(i, val, cur*2+1, mid+1, r)
        self.seg[cur] = max(self.seg[cur*2], self.seg[cur*2+1])
    
    def _query(self,ql,qr,cur,l,r):
        if ql<=l and qr >=r:
            return self.seg[cur]
        mid = (l + r) // 2
        max_gap = 0
        if ql <= mid:
            max_gap = max(max_gap, self._query(ql, qr, cur * 2, l, mid))
        if qr > mid:
            max_gap = max(max_gap, self._query(ql, qr, cur * 2 + 1, mid + 1, r))
        return max_gap

    def insert(self, idx, val):
        self._insert(idx, val, 1, 0, self.size)

    def query(self, left, right):
        return self._query(left, right, 1, 0, self.size)

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        rmax = 500005

        #st = Solution(rmax)
        slist = SortedList([0, rmax])
        self.insert(rmax, rmax)

        ans= []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = slist.bisect_left(x)
                l = slist[i-1]
                r = slist[i]

                slist.add(x)

                self.insert(x, x-l)
                self.insert(r, r-x)

            else:
                x, size = q[1], q[2]

                i = slist.bisect_right(x) -1
                prev = slist[i]

                max_gap = self.query(0, prev)
                max_gap = max(max_gap, x-prev)

                ans.append(size<=max_gap)
        return ans