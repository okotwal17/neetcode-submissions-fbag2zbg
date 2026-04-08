import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[len(nums) - k:]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if self.heap[0] and val < self.heap[0]:
            return self.heap[0]
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        return self.heap[0] 
        
