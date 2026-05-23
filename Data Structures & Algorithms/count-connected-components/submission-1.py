class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #Hashmap -> Holds the edges
        adj = defaultdict(list)

        for pre, nxt in edges:
            adj[nxt].append(pre)
            adj[pre].append(nxt)

        #Initialize count
        self.count = 0
        
        #visit set
        visit = set()
        
        #DFS
        def dfs(curr):

            #Base cases: In visit
            if curr in visit:
                return

            #Put in Visit
            visit.add(curr)

            #Loop through neighbors
            for nxt in adj[curr]:
                dfs(nxt)


        #Loop through nodes not in visit
        for i in range(n):
            if i not in visit:
                self.count += 1
                dfs(i)
        
        return self.count