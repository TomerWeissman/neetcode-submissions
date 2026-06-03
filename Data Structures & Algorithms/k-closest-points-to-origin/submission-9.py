import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDistance(point):

            x, y = point
            d = math.sqrt(x**2 + y **2)

            return [d, [x, y]]
        
        heap = []

        for point in points:
            point = getDistance(point)
            heapq.heappush(heap, point)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap))
        
        return [ele[1] for ele in res]




'''
1. get distance

2. run through all

3. push all into heap

4. 


'''