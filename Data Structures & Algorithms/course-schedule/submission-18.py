class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mapping = {i:[] for i in range(numCourses)}
        for nxt, pre in prerequisites:
            mapping[pre].append(nxt)
        
        visit = set()
        def dfs(crs):
            if mapping[crs] == []:
                return True
            
            if crs in visit:
                return False
            
            visit.add(crs)
            for nxt in mapping[crs]:
                if not dfs(nxt): return False
                mapping[nxt] = []
            visit.remove(crs)
            
            return True
        

        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
            
