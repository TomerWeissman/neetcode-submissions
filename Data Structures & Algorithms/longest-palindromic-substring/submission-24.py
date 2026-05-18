class Solution:
    def longestPalindrome(self, s: str) -> str:

        def pal_length(l, r):

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            
            return (r-1)-(l+1)+1, [l+1, r-1]
        
        resLen, res = float('-inf'), [-1, -1]
        for i in range(len(s)):
            
            odd_resLen, odd_res = pal_length(i-1,i+1)
            if odd_resLen > resLen:
                resLen = odd_resLen
                res = odd_res

            even_resLen, even_res = pal_length(i,i+1)
            if even_resLen > resLen:
                resLen = even_resLen
                res = even_res
            
        
        l, r = res
        return s[l:r+1]





        






        