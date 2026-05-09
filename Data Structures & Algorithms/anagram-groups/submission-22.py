class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for s in strs:
            mapper = [0 for i in range(26)]
            for c in s:
                mapper[ord(c) - ord('a')] += 1
            
            hashmap[tuple(mapper)].append(s)
        
        return list(hashmap.values())

        