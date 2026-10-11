class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v,t))
        distanceMap = {}
        for i in range(1, n + 1):
            distanceMap[i] = float("inf")
        pq = []
        heapq.heappush(pq,(0, k))
        visited = set()
        while pq and len(visited) != n:
            timeFromSrc, curNode = heapq.heappop(pq)
            if curNode in visited:
                continue
            distanceMap[curNode] = timeFromSrc
            visited.add(curNode)
            for neighbor, time in adjList[curNode]:
                if timeFromSrc + time < distanceMap[neighbor]:
                    heapq.heappush(pq, (timeFromSrc + time, neighbor))
        return max(distanceMap.values()) if len(visited) == n else -1
        
