class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(r, c, i):

            if (
                min(r,c) < 0 or
                r == len(board) or
                c == len(board[0]) or
                board[r][c] != word[i] or 
                i >= len(word) or 
                (r,c) in visit
                ):

                return False
            
            if i == len(word) - 1:
                return True
            
            i += 1
            visit.add((r,c))

            outcome = (
                backtrack(r-1, c, i) or
                backtrack(r+1, c, i) or
                backtrack(r, c-1, i) or
                backtrack(r, c+1, i)
                )
            visit.remove((r,c))
            i -= 1
            return outcome
        
        visit = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        
        return False


