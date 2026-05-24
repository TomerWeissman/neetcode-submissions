"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)


        for i in range(1, len(intervals)):

            first = intervals[i-1]
            second = intervals[i]

            if first.end > second.start:
                return False
        
        return True





'''
1. sort based on start times

2. loop through

    2a. if end1 > start2:
        return False
    
3. return True

'''
