class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            s1, e1 = res[-1]
            s2, e2 = intervals[i]

            if e1 >= s2:

                s1 = min(s1, s2)
                e1 = max(e1, e2)
                res[-1] = [s1, e1]
            else:
                res.append([s2, e2])
        
        return res

        



'''
1. sort the intervals

2. go through the intervals

    2a. if max1 > min2:

        2aa. newInterval = min(from min), max(from max)
    

'''
        