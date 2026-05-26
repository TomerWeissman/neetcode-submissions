from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preDict = defaultdict(list)

        for nxt, pre in prerequisites:
            preDict[nxt].append(pre)

        visit = set()

        def dfs(crs):

            if crs in visit:
                return False

            if preDict[crs] == []:
                return True

            visit.add(crs)

            for n in preDict[crs]:
                if not dfs(n):
                    return False
            
            visit.remove(crs)
            preDict[crs] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


