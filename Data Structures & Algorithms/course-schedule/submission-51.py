from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #hashmap: stores pres and nxt
        preDict = defaultdict(list)

        for nxt, pre in prerequisites:
            preDict[nxt].append(pre)

        visit = set()
        
        #dfs
        def dfs(curr):

            #curr in visit: False, curr no nei: True
            if curr in visit:
                return False
            
            if preDict[curr] == []:
                return True

            #visit add
            visit.add(curr)

            for nei in preDict[curr]:
                if not dfs(nei):
                    return False

            #visit remove
            visit.remove(curr)
            preDict[curr] = []
            return True
        

        #loop all courses:
        for i in range(numCourses):
            
            if not dfs(i):
                return False
        
        return True
