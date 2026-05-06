class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == len(grid) or
                c == len(grid[0]) or
                grid[r][c] == '0' or 
                (r, c) in visited
                ):
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        visited = set()
        islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited and grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1
        
        return islands

