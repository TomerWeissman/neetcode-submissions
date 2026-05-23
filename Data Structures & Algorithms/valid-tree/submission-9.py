class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        '''
        Check if there are loops.
        '''

        #Create hashmap of connections -> connections[node] = [n1, n2, n3, ...]

        connections = defaultdict(list)

        for pre, nxt in edges:
            connections[pre].append(nxt)
            connections[nxt].append(pre)

        #loop through nodes
            #if node not in connection -> False

        if len(edges) > (n-1):
            return False

        #create visit set
        visit = set()

        #Create dfs

        #DFS
        def dfs(prev, curr):

            #base cases: in visit -> return False
            
            if curr in visit:
                return False

            #add to visit
            visit.add(curr)

            #loop through nbs
            for nxt in connections[curr]:

                #if dfs(neighbor) False:
                    #return False
                
                if nxt == prev:
                    continue

                if not dfs(curr, nxt):
                    return False
                
            return True
        
        return dfs(-1, 0) and len(visit) == n
        

            





        