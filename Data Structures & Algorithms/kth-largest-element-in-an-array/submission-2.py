import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k >= 0:
            heapq.heappop(nums)
            k-=1
        return nums[0]