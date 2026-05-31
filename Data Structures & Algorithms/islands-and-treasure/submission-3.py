class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(r, c):

            queue = deque()
            queue.append((r, c))
            visit = set()
            visit.add((r,c))
            neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
            distance = 0
            
            while queue:
                distance += 1
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in neighbors:
                        row = r + dr
                        col = c + dc

                        if not (
                            min(row, col) < 0 or
                            row == len(grid) or
                            col == len(grid[0]) or
                            grid[row][col] == -1 or
                            (row,col) in visit
                            ):

                            if grid[row][col] == 0:
                                return distance
                            
                            queue.append((row,col))
                            visit.add((r,c))
            
            return float('inf')
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    grid[row][col] = bfs(row, col)
        



                    



'''
1. create a bfs function

    1a. create queue, visit

    1b. wbile queue

        1ba. for i in range queue

            1baa. go around and add all the nieghbors

            1bab. if neighbor is treasure chest, return with the value

            1bab. if the neighbor passes, then add to queue
        
        1bb. add 1 to distance.
    
    return inf

2. run bfs for every land cell


'''
        