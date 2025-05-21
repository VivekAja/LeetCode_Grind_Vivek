#BruteForce
#TC: O(n * m * (n + m)) ≈ O(n^2 * m + n * m^2)
#SC: O(n * m)
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

---------------------------------------------------------------
#BruteForce
#TC: O(m * n)
#SC: O(k), where k = number of unique zero positions → O(m + n) in worst case
Using Set 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        zero_set = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_set.add((r,c))

        print(zero_set)
        for r,c in zero_set:
            for col in range(cols):
                if matrix[r][col] != 0:
                    matrix[r][col] = 0
            for row in range(0, rows):
                if matrix[row][c] != 0:
                    matrix[row][c] = 0      
        return

---------------------------------------------------------------
#BruteForce
#TC: O(m * n)
#SC: O(m + n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        row = [False]*m
        col = [False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True     
        for i in range(m):
            for j in range(n):
                if row[i] == True or col[j] == True:
                    matrix[i][j] = 0

---------------------------------------------------------------
#Optimal
#TC: O(n*m)
#Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstrow = False
        firstcol = False

        #Check if firstcol is impacted
        for i in range(m):
            if matrix[i][0] ==0:
                firstcol = True
                break

        #Check if firstrow is impacted
        for j in range(n):
            if matrix[0][j] ==0:
                firstrow = True
                break

        #Setting Markers
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if firstrow:
            for j in range(n):
                matrix[0][j] = 0

        if firstcol:
            for i in range(m):
                matrix[i][0] = 0
        
========================================================================================


        
