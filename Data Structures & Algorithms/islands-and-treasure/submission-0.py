class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        def addCell(r, c):

            if (r >= ROWS or r < 0 or
                c >= COLS or c < 0 or 
                (r,c) in visited or grid[r][c] == -1):
                return
            
            q.append((r,c))
            visited.add((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()  
                grid[r][c] = distance

                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    addCell(r + nr, c + nc)
                
            distance += 1