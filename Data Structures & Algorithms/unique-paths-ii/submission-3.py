class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        hashmap = {}

        def dfs(r, c):
            if (
                r == len(obstacleGrid) or
                c == len(obstacleGrid[0]) or
                obstacleGrid[r][c] == 1
                ):
                return 0
            
            if (r,c) in hashmap:
                return hashmap[(r,c)]
            
            if (
                r == len(obstacleGrid) - 1 and
                c == len(obstacleGrid[0]) - 1
                ):
                return 1
            
            hashmap[(r,c)] = dfs(r+1, c) + dfs(r,c+1)
            return hashmap[(r,c)]
        
        return dfs(0, 0)


        