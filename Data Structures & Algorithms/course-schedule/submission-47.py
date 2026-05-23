

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #edge cases: no prereq, 
        if not prerequisites:
            return True
        
        #create map for prerequisites
        preDict = defaultdict(list)

        for nxt, pre in prerequisites:
            preDict[nxt].append(pre)

        visit = set()
        #dfs function
        def dfs(crs):

            #base cases: hit itself, hit none, in visit
                #return false
            
            if crs in visit:
                return False
            
            if not preDict[crs]:
                return True

            visit.add(crs)
            #loop through next nodes
            for pre in preDict[crs]:

                #dfs for node
                #return false if false
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preDict[crs] = []

            return True
        
        #loop numcourses
        for i in range(numCourses):
            
            #run dfs -> false: return False

            if not dfs(i):
                return False
        
        return True


            


