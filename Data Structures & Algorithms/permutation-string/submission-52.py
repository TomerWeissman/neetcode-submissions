class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False

        freq, window = [0]*26, [0]*26

        for c in s1:
            freq[ord(c) - ord('a')] += 1
        
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        
        if window == freq:
            return True
        
        l, r = 0, len(s1) - 1

        while r < len(s2) - 1:

            window[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            window[ord(s2[r]) - ord('a')] += 1

            if window == freq:
                return True
        
        return False

            
            



'''
EDGE CASE: s2 is shorter than s1, return false


1. create a dp that has the frequency of the letters

2. cycle through with a window of length of s1

    3. the window should have a dp too

    4. if they are equal, return true.

5. return false





'''
        