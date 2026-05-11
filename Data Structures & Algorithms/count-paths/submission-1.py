class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        hashmap = {}

        def dfs(r, c):
            if (
                r == m or
                c == n
                ):
                return 0

            if (r,c) in hashmap:
                return hashmap[(r,c)]

            if (
                r == m - 1 and
                c == n - 1
                ):
                return 1

            
            hashmap[(r, c)] = dfs(r+1, c) + dfs(r, c+1)
            
            return hashmap[(r,c)]   

        return dfs(0, 0)

    

        