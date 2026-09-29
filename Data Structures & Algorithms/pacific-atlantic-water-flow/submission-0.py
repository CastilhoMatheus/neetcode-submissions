class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atla = set()
        paci = set()
        ROWS, COLS = len(heights), len(heights[0])

    
        def dfs(r, c, ocean, minHeight):
            if ((r,c) in ocean or r == ROWS or r < 0 or 
                c == COLS or c < 0 or heights[r][c] < minHeight):
                return 
        
            ocean.add((r,c))

            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])


        for c in range(COLS):
            dfs(0, c, paci, heights[0][c])
            dfs(ROWS - 1, c, atla, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, paci, heights[r][0])
            dfs(r, COLS-1, atla, heights[r][COLS-1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atla and (r,c) in paci:
                    res.append([r,c])
        
        return res