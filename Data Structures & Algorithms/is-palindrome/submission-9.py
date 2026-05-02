class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalnum()])
        print(s)
        
        palsize = len(s) // 2

        r = len(s) - 1
        l = 0

        while l <= palsize and s:
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
        