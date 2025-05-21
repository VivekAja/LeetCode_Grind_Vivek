import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        temp[i][k] = 0 #Marking row as 0
                    for l in range(m):
                        temp[l][j] = 0 #Marking col as 0         
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]

        