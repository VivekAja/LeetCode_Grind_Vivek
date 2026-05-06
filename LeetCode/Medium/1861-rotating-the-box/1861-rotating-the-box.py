class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #m, n = len(boxGrid), len(boxGrid[0])

        transposed = [[boxGrid[row][col] for row in range(len(boxGrid))] for col in range(len(boxGrid[0]))]
        """
        for row in transposed:
            for col in transposed:
                transposed[row][col], transposed[col][row] = transposed[col][row], transposed[row][col]
        print(f"Rotated {transposed}")
        """
        rotated = [row[::-1] for row in transposed]
        #print(rotated)
        num_rows = len(rotated)
        num_cols = len(rotated[0])

        for col in range(num_cols-1, -1, -1):
            for row in range(num_rows-1, -1 , -1):
                """
                if rotated[row][col] == "#" and rotated[row-1][col] == "." and row != 0:
                    rotated[row][col], rotated[row-1][col] = rotated[row-1][col], rotated[row][col]
                    print(row, col)
                if row == 0 and rotated[row][col] == "#" and rotated[row+1][col] == ".":
                    rotated[row][col], rotated[row+1][col] = rotated[row+1][col], rotated[row][col]
                    print(row, col)

                """
                if rotated[row][col] == "#":
                    next_row = row
                    while next_row + 1 < num_rows and rotated[next_row + 1][col] == ".":
                        next_row += 1
                    if next_row != row:
                        rotated[row][col], rotated[next_row][col] = rotated[next_row][col], rotated[row][col]
                        
                
                    
        return rotated

