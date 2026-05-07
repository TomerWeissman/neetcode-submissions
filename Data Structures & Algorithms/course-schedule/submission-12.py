class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        for nxt, prev in prerequisites:
            adj_list[prev].append(nxt)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            
            if adj_list == []:
                return True


            visit.add(crs)
            for n in adj_list[crs]:
                if not dfs(n): return False
            visit.remove(crs)
            adj_list[crs] = []

            return True
        
        
        for start in range(numCourses):
            if not dfs(start): return False
        
        return True
    




        