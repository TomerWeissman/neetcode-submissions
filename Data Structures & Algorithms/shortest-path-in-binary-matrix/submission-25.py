class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        visit = set()
        queue = deque()
        queue.append((0, 0))
        length = 1

        while queue:
            for i in range(len(queue)):                
                r, c = queue.popleft()
                
                if (r == len(grid) - 1 and
                    c == len(grid[0]) - 1
                    ):
                    return length

                neighbors = []
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if [x,y] != [0,0]:
                            neighbors.append([x,y])


                for dr, dc in neighbors:

                    nr = r + dr
                    nc = c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr == len(grid) or
                        nc == len(grid) or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                        ):
                        continue
                
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr,c+dc))
                
            length += 1
        
        return -1

        

            

            

        