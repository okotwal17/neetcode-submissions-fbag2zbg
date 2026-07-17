class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if s1 == s2:
                continue
            else:
                s1 -= s2
                heapq.heappush(heap, -s1)
        return -heap[0] if len(heap) == 1 else 0