class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows check

        for r in range(9):
            valid_row = set()
            for c in range(9):
                if board[r][c] != '.' and board[r][c] in valid_row:
                    return False
                
                valid_row.add(board[r][c])

        #col check
        c = 0
        while c < 9:
            r = 0
            valid_col = set()

            while r < 9:
                if board[r][c] != '.' and board[r][c] in valid_col:
                    return False
                
                valid_col.add(board[r][c])
                r += 1
            
            c += 1
        # Grid check
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True
