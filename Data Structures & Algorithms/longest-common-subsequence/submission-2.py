class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        hashmap = {}

        def dfs(r, c):
            
            if (
                r == len(text1) or
                c == len(text2)
                ):
                return 0
            
            if (r,c) in hashmap:
                return hashmap[(r,c)]
            
            if text1[r] == text2[c]:
                hashmap[(r,c)] = 1 + dfs(r+1,c+1)
                return hashmap[(r,c)]
            else:
                hashmap[(r,c)] = max(dfs(r+1,c), dfs(r,c+1))
                return hashmap[(r,c)]
        
        return dfs(0, 0)
        

            
            



        