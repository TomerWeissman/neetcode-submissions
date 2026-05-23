class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        #Create adjacency list
        #Check if any invalid (a is prefix of b and b is longer)

        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break


        #Depth first search through adj list
        #If circle back, return false

        visit = {}
        res = []
        
        def dfs(c):

            #basecases: if in visit.
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for char in adj[c]:
                if dfs(char):
                    return True
            
            visit[c] = False
            res.append(c)
        
        for char in adj:
            if dfs(char):
                return ""
        
        res.reverse()
        return ''.join(res)



        #Loop through adj list and try all starts.







