import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Creating DSU
        rank = [-1] * len(points)
        #Don't need points to map to, points is already the given list
        def find(node):
            if rank[node] < 0:
                return node
            rank[node] = find(rank[node])
            return rank[node]
        def union(n1, n2):
            n1,n2 = find(n1), find(n2)
            #If in same disjoint set, return True for in same set
            if n1 == n2:
                return True
            #Else combine and return False
            totalSize = rank[n1] + rank[n2]
            if rank[n1] < rank[n2]:
                rank[n2] = n1
                rank[n1] = totalSize
            else:
                rank[n1] = n2
                rank[n2] = totalSize
            return False
        

        #Create PriorityQ elems
        priorityQ = []
        for p1 in range(len(points)):
            for p2 in range(p1+1, len(points)):
                point1, point2 = points[p1], points[p2]
                toAdd = [abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]), [p1, p2]]
                priorityQ.append(toAdd)
        heapq.heapify(priorityQ)

        res = 0
        while priorityQ:
            curElem = heapq.heappop(priorityQ)
            dist, indices = curElem[0], curElem[1]
            if not union(indices[0], indices[1]):
                res+=dist
        return res

            


