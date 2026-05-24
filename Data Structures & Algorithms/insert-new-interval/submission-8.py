class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        print(intervals)

        for i in range(0, len(intervals)):
            start1, end1 = newInterval
            start2, end2 = intervals[i]
            
            if end1 < start2:
                res.append(newInterval)
                res += intervals[i:]
                return res
            elif start1 > end2:
                res.append(intervals[i])
            else:
                newInterval = [min(start1, start2), max(end1, end2)]

        res.append(newInterval)
        return res




'''
init:
- res = []

1. loop through intervals

    1a. if end1 < start2:
        1aa. append int2
        return
    1b. if start1 > end2
        1ba. append int1
    1c. else:
        1ca. newInterval = [min(s1,s2), max(e1,e2)

2. return res.append(newItnerval)


'''
