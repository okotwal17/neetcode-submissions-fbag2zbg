import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Have distance = x^2 + y^2
        maxHeap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(maxHeap, (dist * -1, tuple(point)))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for ele in maxHeap:
            res.append(list(ele[1]))
        return res