class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        disjoint = [-1] * len(points)
        def find(n):
            if disjoint[n] < 0:
                return n
            disjoint[n] = find(disjoint[n])
            return disjoint[n]

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return False
            totalSize = disjoint[n1] + disjoint[n2]
            if disjoint[n1] < disjoint[n2]:
                disjoint[n2] = n1
                disjoint[n1] = totalSize
            else:
                disjoint[n1] = n2
                disjoint[n2] = totalSize
            return True
        

        heap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                manhattan = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heap.append((manhattan, i, j))
        heapq.heapify(heap)
        numConnect = len(points)
        res = 0
        while numConnect > 1:
            dist, p1, p2 = heapq.heappop(heap)
            if union(p1, p2):
                numConnect -= 1
                res += dist
        return res
