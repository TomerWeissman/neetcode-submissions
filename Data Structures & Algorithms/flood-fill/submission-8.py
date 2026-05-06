class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        bef = image[sr][sc]
        aft = color
        r, c = sr, sc

        def dfs(image, r, c, bef, aft):
            if (
                min(r, c) < 0 or
                r == len(image) or 
                c == len(image[0]) or
                (r,c) in visited or
                image[r][c] != bef
                ):
                return
            
            visited.add((r, c))
            image[r][c] = aft
            dfs(image, r+1, c, bef, aft)
            dfs(image, r-1, c, bef, aft)
            dfs(image, r, c+1, bef, aft)
            dfs(image, r, c-1, bef, aft)
            visited.remove((r,c))
        
        dfs(image, r, c, bef, aft)
        return image


