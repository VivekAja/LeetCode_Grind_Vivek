class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        #flat = [0]*(m*n)
        if m*n != r*c:
            return mat
        new_mat = [[0] * c for _ in range(r)]

        for i in range(m*n):
            sr = i // n
            sc = i % n

            tr = i // c
            tc = i % c

            new_mat[tr][tc] = mat[sr][sc]
        return new_mat
        
