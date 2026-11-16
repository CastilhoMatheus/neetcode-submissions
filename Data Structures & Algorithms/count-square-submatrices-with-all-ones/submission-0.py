class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = [[0] * (COLS) for _ in range(ROWS)]

        total = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    total += dp[r][c]
            
        return total
        

