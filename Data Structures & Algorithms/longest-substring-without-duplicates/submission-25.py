class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        l = 0
        r = -1

        length = 0

        while r < len(s) - 1:
            r += 1
            freq[s[r]] += 1


            while freq[s[r]] > 1 and l < r:
                freq[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)


        return length

        

