class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            maxElem = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, maxElem)
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            maxElem, minElem = -heapq.heappop(self.maxHeap), heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -minElem)
            heapq.heappush(self.minHeap, maxElem)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]
        
        