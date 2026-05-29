class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        nums.sort()

        def backtrack(i):

            if i >= len(nums):
                if path not in res:
                    res.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res



'''
1. create backtrack

    1a. if i > len(nums):
        append path
        return
    
    1b. add next, run with following

    1c. remove next, run with following

2. run

'''
        