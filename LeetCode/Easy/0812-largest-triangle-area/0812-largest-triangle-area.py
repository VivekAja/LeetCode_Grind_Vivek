class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        area = 0.0
        for i in range(n):
            xa, ya = points[i]
            for j in range(i+1, n):
                xb, yb = points[j]
                for k in range(j+1, n):
                    xc, yc = points[k]
                    mulA = xa * (yb-yc) + xb * (yc - ya) + xc * (ya-yb) 
                    area = max(0.5 * abs(mulA), area)
                
        return area