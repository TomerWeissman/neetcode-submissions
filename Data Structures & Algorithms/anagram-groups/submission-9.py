class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            mapping = [0]*26
            for c in string:
                mapping[ord(c) - ord('a')] += 1
            
            res[tuple(mapping)].append(string)
        return list(res.values())
        
            
        
        