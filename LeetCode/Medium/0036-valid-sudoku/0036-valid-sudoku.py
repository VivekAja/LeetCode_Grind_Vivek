class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        for i in range(0,9,3):   
            for j in range(0,9,3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        if board[k+i][l+j] in s:
                            return False
                        elif board[k+i][l+j] != '.':
                            s.add(board[k+i][l+j])
        return True