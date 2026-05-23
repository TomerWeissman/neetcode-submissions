class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #create visit set
        visit = set() #O(1)
        count = 0 #O(1)
        neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)] #O(1)

        #DFS
        def dfs(count, r, c):
            #positive basecase:
                ##length of path is eqaul to word
            
            if count == len(word): #O(1)
                return True

            #basecases:
                #if letter is not equal
                #if off board
                #if going back to prev
            
            #O(1)
            if (
                min(r,c) < 0 or
                r == len(board) or
                c == len(board[0]) or
                (r,c) in visit or
                word[count] != board[r][c]
                ):
                return
            
            #add to visit
            visit.add((r,c)) #O(1)

            #add letter to count
            count += 1 #O(1)

            #loop though neighbors with dfs
            for dr, dc in neighbors: #O(4)
                row = r + dr
                col = c + dc

                if dfs(count, row, col): #O(4w)
                    return True

            #remove from visit
            visit.remove((r,c))
            #remove count
            count -= 1
        
        #loop through all letters, if first, start dfs

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(0, row, col):
                        return True
            
        return False


