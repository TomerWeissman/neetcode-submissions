import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(tup):
            x = tup[0]
            y = tup[1]
            return math.sqrt((x)**2 + (y)**2)
        
        d_points = [(distance(point), point) for point in points]
        print(d_points)
        heapq.heapify(d_points)
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(d_points)[1])
        
        return res

