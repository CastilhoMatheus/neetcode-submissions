class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0

        def traverse(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))

            count = 1
            for dr, dc in directions:
                cur = traverse(r + dr, c + dc)
                count += cur
            
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    i_a = traverse(r,c)
                    res = max(res, i_a)

        return res