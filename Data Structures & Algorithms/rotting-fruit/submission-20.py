from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        neighbors  = [(0,1), (0,-1), (1,0), (-1,0)]
        self.rotted = 0
        self.minutes = -1

        def bfs(queue):

            while queue:
                
                for _ in range(len(queue)):

                    row, col = queue.popleft()

                    for dc, dr in neighbors:
                        r = dr + row
                        c = dc + col

                        if (
                            min(c, r) < 0 or
                            r == len(grid) or
                            c == len(grid[0]) or
                            grid[r][c] != 1
                            ):
                            continue
                        
                        queue.append((r,c))
                        grid[r][c] = 2
                        self.rotted += 1
                
                self.minutes += 1
        

        fresh = 0
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row,col))
        
        if fresh == 0:
            return 0
        bfs(queue)

        if fresh == self.rotted:
            return self.minutes
        
        return -1



    





'''
BFS FUNCTION:

1. while queue

    1a. for _ in range(len(queue))

    1b. curr = queue.popleft()

    1c. for neighbor of curr

        1ca. if neighbor valid, append.
        1cb. turn neighbor into 2
        1cc. rotted -> increment
    
    1d. add a minute


2. run through everything, find number of fresh, and place of 2s

3. run bfs

4. if fresh == rotted, return minutes




- find how many fresh



'''
        