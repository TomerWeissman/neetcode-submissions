class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {}
        def search(i):
            
            if i == len(s):
                return 1
            
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0
            
            res = search(i+1)

            if (
                i + 1 < len(s) and
                (s[i] == '1' or 
                (s[i] == '2' and s[i+1] in '0123456')
            )):
                res += search(i + 2)
            
            dp[i] = res
            return dp[i]
        
        return search(0)
            
            
            