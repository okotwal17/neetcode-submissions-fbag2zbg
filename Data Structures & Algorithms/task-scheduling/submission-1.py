import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [freq[v] * -1 for v in freq]
        print(maxHeap)
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while maxHeap or q:

            if maxHeap:
                temp = heapq.heappop(maxHeap) * -1 - 1
                if temp:
                    q.append((time + n, temp))
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1] * -1)
            time += 1
        return time
