class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        outcome = []

        def backtrack(i, path, total):

            if total > target:
                return
            
            if total == target:
                outcome.append(path[:])
                return
            

            for x in range(i,len(candidates)):
                if x > i and candidates[x] == candidates[x-1]:
                    continue
                
                path.append(candidates[x])
                total += candidates[x]
                backtrack(x+1, path, total)
                path.pop()
                total -= candidates[x]

        backtrack(0, [], 0)
        return outcome


        