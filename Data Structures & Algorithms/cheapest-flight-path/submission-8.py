class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf")] * n
        distance[src] = 0
        for i in range(k + 1):
            newDistance = distance.copy()
            for u, v, p in flights:
                if distance[u] == float("inf"):
                    continue
                if distance[u] + p < newDistance[v]:
                    newDistance[v] = distance[u] + p
            distance = newDistance
        return distance[dst] if distance[dst] != float("inf") else -1