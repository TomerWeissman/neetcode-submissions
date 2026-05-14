class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        path = []

        def backtrack(i, open_, close_):

            if i >= 2*n:
                res.append(''.join(path[:]))
                return
            
            if open_ < n:
                path.append('(')
                backtrack(i+1, open_+1, close_)
                path.pop()
            
            if close_ < open_:
                path.append(')')
                backtrack(i+1, open_, close_+1)
                path.pop()
        
        backtrack(0, 0, 0)
        return res

        

        