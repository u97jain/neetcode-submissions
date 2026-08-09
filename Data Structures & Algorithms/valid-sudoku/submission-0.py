class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for row
        for col in range(9):
            rowSet = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowSet:
                    return False
                rowSet.add(board[row][col])
        
        #for column
        for row in range(9):
            colSet = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in colSet:
                    return False
                colSet.add(board[row][col])

        #for 3x3 square
        for square in range(9):
            sqSet = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) *3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sqSet:
                        return False
                    sqSet.add(board[row][col])

        return True
        