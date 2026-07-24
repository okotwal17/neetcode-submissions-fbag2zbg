class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top, bottom = 0, cost[-1]
        for i in range(len(cost) - 2, -1, -1):
            top, bottom = bottom, cost[i] + min(top, bottom)
        return min(top, bottom)
        