# Valid Sudoku

class Solution:
    def isDuplicate(self, vals):
        cleaned_vals = [val for val in vals if val != '.']
        return len(cleaned_vals) == len(set(cleaned_vals)) 
    
    
    def isValidSudoku(self, board):
        for row in board:
            if not self.isDuplicate(row):
                return False
        
        for column in zip(*board):
            if not self.isDuplicate(column):
                return False
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = [board[i+row_offset][j+column_offset] for row_offset in range(3) for column_offset in range(3)]
                if not self.isDuplicate(box):
                    return False
        return True
        
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
            
obj = Solution()
print(obj.isValidSudoku(board))

# Time Complexity O(1)
# Space Complexity O(1)