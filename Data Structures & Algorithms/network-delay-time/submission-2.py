class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))
        distanceMap = {}
        for i in range(1, n + 1):
            distanceMap[i] = float("inf")
        heap = [(0, k)]
        visited = set()
        while heap and len(visited) != n:
            curTime, curNode = heapq.heappop(heap)
            if curNode in visited:
                continue
            visited.add(curNode)
            distanceMap[curNode] = curTime
            for node, time in adjList[curNode]:
                heapq.heappush(heap, (curTime + time, node))
        print(distanceMap.values())
        res = max(distanceMap.values())
        return res if res != float("inf") else -1
            