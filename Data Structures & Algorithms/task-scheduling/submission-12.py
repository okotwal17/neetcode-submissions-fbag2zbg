class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
     #We have a priority queue/heap to decide to process the most frequent element.
     #Then we have a queue for waiting n cycles.
        counter = Counter(tasks)
        heap = [-cnt for val, cnt in counter.items()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            if heap:
                elem = heapq.heappop(heap)
                if elem + 1:
                    q.append((time + n, elem + 1))
            if q and q[0][0] == time:
                t, cnt = q.popleft()
                heapq.heappush(heap, cnt)
            time += 1
        return time
