import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = ((x**2) + (y**2)) * -1
            heapq.heappush((dist, points[i]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x_y = heapq.heappop(maxHeap)
            res.append(x_y)
        return re
        