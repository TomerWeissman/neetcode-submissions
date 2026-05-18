class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROW = len(grid)
        COL = len(grid[0])
        nbs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visit = set()

        def cover_island(r, c):

            if (
                min(r,c) < 0 or
                r == ROW or
                c == COL or
                (r,c) in visit or
                grid[r][c] == '0'
                ):
                return
            
            visit.add((r,c))

            for dr, dc in nbs:
                row = dr + r
                col = dc + c
                cover_island(row, col)
        
        islands = 0

        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in visit and grid[r][c] == '1':
                    islands += 1
                    cover_island(r, c)
        
        return islands


