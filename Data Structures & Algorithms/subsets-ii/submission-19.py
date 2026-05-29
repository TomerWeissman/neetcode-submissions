class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = set()
        path = []

        def backtrack(i):

            if i >= len(nums):
                res.add(tuple(path[:]))
                return
            
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
        
        nums.sort()
        backtrack(0)
        return [list(s) for s in res]



'''
1. create backtrack

    1a. if i > len(nums):
        append path
        return
    
    1b. add next, run with following

    1c. remove next, run with following

2. run

'''
        