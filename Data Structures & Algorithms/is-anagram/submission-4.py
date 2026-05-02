class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = defaultdict(int)
        t_hashmap = defaultdict(int)

        for ls in list(s):
            s_hashmap[ls] += 1
        for lt in list(t):
            t_hashmap[lt] += 1
        

        if s_hashmap == t_hashmap:
            return True
        
        return False

        