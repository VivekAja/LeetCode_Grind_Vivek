import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        print(m, n)
        heap = []
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count +=1
            heap.append((count, i))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result