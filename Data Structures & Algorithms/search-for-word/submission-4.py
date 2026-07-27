class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set() #(r, c)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r, c, i):
            res = False

            if i == len(word):
                return True

            if (
                r < ROWS and c < COLS and
                r >= 0 and c >= 0 and
                (r, c) not in path and
                board[r][c] == word[i] 
                ):

                path.add((r, c))

                for d in directions:
                   res = res or backtrack(r + d[0], c + d[1], i + 1)
                
                path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        
        return False