class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, resLen = [], len(nums)
        visit = []

        def backtrack():

            if len(visit) == resLen:
                res.append(visit[:])
            
            for i in range(resLen):

                if nums[i] not in visit:
                    visit.append(nums[i])
                    backtrack()
                    visit.pop()
        
        backtrack()
        return res


    



'''
1. Backtracking algo

    1a. if the path is length of required, add to res

    1b. for all letters

        1ba. if letter not in path

        1bb. add to visit

        1bc. run dfs

        1bd. remove from visit

2. return res




'''
        