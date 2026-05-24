class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        intervals.sort()
        print(intervals)

        for i in range(1, len(intervals)):
            s1, e1 = intervals[i-1]
            s2, e2 = intervals[i]

            if e1 > e2:
                count += 1
            elif e1 > s2:
                count += 1
                intervals[i] = intervals[i-1]
        
        return count




'''
1. loop through intervals

    2a. if e1 >= e2 -> delete first
        count += 1
    2b. if e1 >= s2 -> delete second
        count += 1
    

return count
'''
        