class Solution:
    def longestPalindrome(self, s: str) -> str:

        def pal_find(l, r):

            while (
                    l >= 0 and
                    r <= len(s) - 1 and
                    s[l] == s[r]
                    ):
                    l -= 1
                    r += 1
            r -= 1
            l += 1
            return r-l+1, [l, r]
        

        resLen, res = float('-inf'), [-1, -1]

        for i in range(len(s)):
            length, outcome = pal_find(i-1, i+1)
            if length > resLen:
                resLen = length
                res = outcome
            length, outcome = pal_find(i, i+1)
            if length > resLen:
                resLen = length
                res = outcome
        
        l, r = res
        print(f'{l}, {r}')
        return s[l:r+1]
            