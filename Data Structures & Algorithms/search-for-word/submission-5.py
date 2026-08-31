class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or 
                board[r][c] != word[i]):
                return False
            
            visited.add((r, c))
            for d in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + d[0], c + d[1]
                if backtrack(nr, nc, i + 1):
                    return True

            visited.remove((r, c))
            return False

        for R in range(ROWS):
            for C in range(COLS):
                if backtrack(R, C, 0):
                    return True
                    
        return False