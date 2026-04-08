import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = [i * -1 for i in stones]
        heapq.heapify(maxStone)
        while len(maxStone) != 1:
            firstHeavy = heapq.heappop(maxStone) * -1
            secondHeavy = heapq.heappop(maxStone) * -1
            if firstHeavy == secondHeavy:
                continue
            else:
                heapq.heappush(maxStone, abs(firstHeavy - secondHeavy) * -1)
        return maxStone[0] * -1