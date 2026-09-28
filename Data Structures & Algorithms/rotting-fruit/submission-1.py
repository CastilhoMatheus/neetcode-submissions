class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque([])
        total = 0

        def addBananas(r,c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or 
                (r,c) in visited or grid[r][c] == 0):
                return 
            
            q.append((r,c))
            visited.add((r,c))
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    total += 1
                
                elif grid[r][c] == 1:
                    total += 1

        if total == 0: return 0
        time = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                total -= 1

                for nr, nc in [(1,0), (-1, 0), (0,1), (0,-1)]:
                    addBananas(r + nr, c + nc)

            time += 1

        return -1 if total else time
