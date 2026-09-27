class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf")] * n
        distance[src] = 0
        for i in range(k + 1):
            new_distance = distance.copy()
            for u, v, p in flights:
                #Not reached here yet
                if distance[u] == float("inf"):
                    continue
                if distance[u] + p < new_distance[v]:
                    new_distance[v] = distance[u] + p
            distance = new_distance
        return distance[dst] if distance[dst] != float("inf") else -1