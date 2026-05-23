class Solution:
    def rob(self, nums: List[int]) -> int:

        #backtrack
        #DFS function; arg: i, end

            #Base case: i > end:
                #return 0
            
            #return max: this house plus skip, next
        
        #run with different ranges

        if len(nums) == 1:
            return nums[0]
        

        def backtrack(i, end, tracker):
            
            if i > end:
                return 0
            
            if i in tracker:
                return tracker[i]
            
            tracker[i] = max(backtrack(i+1, end, tracker), nums[i] + backtrack(i+2, end, tracker))
            
            return tracker[i]
        
        tracker_a = defaultdict(int)
        tracker_b = defaultdict(int)
        return max(backtrack(0, len(nums)-2, tracker_a), backtrack(1, len(nums)-1, tracker_b))
            
        