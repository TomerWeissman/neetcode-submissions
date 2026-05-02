class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        max_len = 0

        l = 0
        r = -1

        while r < len(s) - 1:
            r += 1
            hashmap[s[r]] += 1
            while hashmap[s[r]] > 1 and l < r:
                hashmap[s[l]] -= 1
                l += 1
            
            print(s[l:r+1])
            max_len = max(r - l + 1, max_len)
        
        return max_len




            

        