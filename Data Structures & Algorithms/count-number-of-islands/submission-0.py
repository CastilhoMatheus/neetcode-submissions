class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        count = 0
        ROW = len(grid)
        COL = len(grid[0])

        def traverse(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROW or c >= COL or
                grid[r][c] == '0'):
                return

            grid[r][c] = '0'

            for dr, dc in directions:
                traverse(r + dr, c + dc)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    traverse(r, c)
                    count += 1

        return count