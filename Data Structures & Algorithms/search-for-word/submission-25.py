class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        l_word = list(word)

        def search(r, c, path, visit):

            if path == l_word:
                return True
            
            if (
                len(path) > len(word) or
                min(r,c) < 0 or
                r == len(board) or
                c == len(board[0]) or 
                (r, c) in visit
                ):
                return False
            
            visit.add((r,c))
            path.append(board[r][c])

            if (
                search(r+1, c, path, visit) or
                search(r-1, c, path, visit) or
                search(r, c+1, path, visit) or
                search(r, c-1, path, visit)
                ):
                return True
            
            path.pop()
            visit.remove((r,c))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if search(row, col, [], set()):
                        return True
        
        return False