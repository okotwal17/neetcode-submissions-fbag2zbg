import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = (x**2) + (y**2)
            minHeap.append((dist, points[i]))
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x_y = heapq.heappop(minHeap)
            res.append(x_y)
            k -= 1
        return res
        