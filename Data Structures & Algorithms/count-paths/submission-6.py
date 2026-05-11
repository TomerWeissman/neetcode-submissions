class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ROW = m
        COL = n
        prevrow = [0 for i in range(COL)]

        for r in range(ROW):
            currow = [0 for i in range(COL)]
            currow[-1] = 1

            for c in range(len(currow) - 2, -1, -1):
                currow[c] = prevrow[c] + currow[c+1]
            
            prevrow = currow
        
        return currow[0]
