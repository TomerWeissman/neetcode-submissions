from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        '''
        1. No islands
        2. No loops
        '''

        adj = defaultdict(list)

        #create adj list
        for prv, nxt in edges:
            adj[prv].append(nxt)
            adj[nxt].append(prv)

        #creat visit set
        visit = set()

        #dfs
        def dfs(prv, curr):

            #basecase: curr in visit (F), no new n (T)
            if curr in visit:
                return False
            
            visit.add(curr)

            #for nei
            for nei in adj[curr]:

                if nei == prv:
                    continue
                #run dfs: If F
                if not dfs(curr, nei):
                    return False
            
            return True
        
        if dfs(-1, 0) and len(visit) == n:
            return True
        
        return False

