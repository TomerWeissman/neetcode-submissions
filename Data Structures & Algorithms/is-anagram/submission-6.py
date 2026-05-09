class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a_hashmap = defaultdict(int)
        b_hashmap = defaultdict(int)

        for i in range(len(s)):
            a_hashmap[s[i]] += 1
            b_hashmap[t[i]] += 1
        
        if a_hashmap == b_hashmap:
            return True
        return False
        


        