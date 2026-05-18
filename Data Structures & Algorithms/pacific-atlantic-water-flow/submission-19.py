class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROW = len(heights)
        COL = len(heights[0])

        self.AT = False
        self.PA = False
        self.i = 0
        def dfs(r, c, pr, pc, visit):

            if (
                min(r, c) < 0 or
                r == ROW or 
                c == COL or
                heights[r][c] > heights[pr][pc] or
                (r, c) in visit
                ):
                return
            
            if r == ROW - 1 or c == COL - 1:
                self.AT = True
            
            if r == 0 or c == 0:
                self.PA = True
            
            visit.add((r,c))
            dfs(r+1, c, r, c, visit)
            dfs(r-1, c, r, c, visit)
            dfs(r, c+1, r, c, visit)
            dfs(r, c-1, r, c, visit)
        
        res = []
        for row in range(ROW):
            for col in range(COL):
                dfs(row, col, row, col, set())
                if self.PA and self.AT:
                    res.append([row, col])
                    self.PA = self.AT = False
        
        return res


            
