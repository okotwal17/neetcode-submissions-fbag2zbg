class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cache = [-1] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if self.cache[i] != -1:
                return self.cache[i]
            self.cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return self.cache[i]
        return min(dfs(0), dfs(1))
