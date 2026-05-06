class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == len(grid) or
                c == len(grid[0]) or
                grid[r][c] == 0 or
                (r, c) in visited
                ):
                return 0
            
            visited.add((r,c))
            count = 1
            count += dfs(r+1,c)
            count += dfs(r-1,c)
            count += dfs(r,c+1)
            count += dfs(r,c-1)

            return count
        
        max_size = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_size = max(max_size, dfs(row, col))

        return max_size

                    
        