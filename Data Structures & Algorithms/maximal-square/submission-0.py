class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        square = 0

        for r in range(R -1, -1, -1):
            for c in range(C -1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
                    square = max(square, dp[r][c])

        return square * square