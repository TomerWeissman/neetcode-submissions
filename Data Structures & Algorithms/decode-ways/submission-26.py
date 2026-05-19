class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}
        
        def search(i):

            if i == len(s):
                return 1
            
            if i > len(s) - 1:
                return 0

            if s[i] == '0':
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = search(i+1)

            if i + 1 < len(s) and (
                s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')
                ):
                dp[i] += search(i+2)

            return dp[i]
        
        return search(0)
