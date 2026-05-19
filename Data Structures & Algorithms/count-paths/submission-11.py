class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        
        def paths(r, c):

            if (
                r == m or
                c == n
                ):
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = paths(r+1, c) + paths(r, c+1)
            return dp[(r,c)]
        
        return paths(0, 0)
            
            