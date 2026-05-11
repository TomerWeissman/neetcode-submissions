class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def square_check(r, c):
            hashmap = defaultdict(int)
            
            for row in range(3):
                for col in range(3):
                    num = board[r+row][c+col]
                    if num != ".":
                        hashmap[num] += 1
                    if hashmap[num] > 1:
                        return False
                
            return True

        def col_check(c):

            hashmap = defaultdict(int)
            
            for num in [board[i][c] for i in range(len(board))]:
                if num != ".":
                    hashmap[num] += 1
                if hashmap[num] > 1:
                    return False
            
            return True
            


        def row_check(r):
            hashmap = defaultdict(int)
            
            for num in board[r]:
                if num != ".":
                    hashmap[num] += 1
                if hashmap[num] > 1:
                    return False
            
            return True

        for row in range(len(board)):
            if not row_check(row):
                return False
        
        for col in range(len(board[0])):
            if not col_check(col):
                return False
        
        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                if not square_check(row, col):
                    return False
        
        return True
        


        