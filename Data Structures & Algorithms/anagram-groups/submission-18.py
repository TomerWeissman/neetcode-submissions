class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            mapping = [0]*26
            for letter in string:
                mapping[ord(letter) - ord('a')] += 1
            
            res[tuple(mapping)].append(string)
        
        return list(res.values())
