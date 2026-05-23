class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        #init hashmap
        adj = {char: set() for word in words for char in word}

        #loop through words -> add adj chars
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            minimum = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            
            for j in range(minimum):
                if word2[j] != word1[j]:
                    adj[word1[j]].add(word2[j])
                    break

        #itit visit, and res
        visit = defaultdict(bool)
        res = []

        #DFS
        def dfs(c):
            #Base: if c in visit
            if c in visit:
                return visit[c]

            #put in visit, init True
            visit[c] = True

            #loop nieghbors
            for nei in adj[c]:
                #DFS
                if dfs(nei):
                    return True

            #Visitfalse
            visit[c] = False
            
            #resappend
            res.append(c)
        
        #loop chars
        for c in adj:

            #DFS
            if dfs(c):
                return ""
        
        #res reverse
        res.reverse()
        
        #return
        return ''.join(res)