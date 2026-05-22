class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def backtrack(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            if curSum == amount:
                return 1
            if curSum > amount or i == len(coins):
                return 0
            dp[(i, curSum)] = backtrack(i, curSum + coins[i]) + backtrack(i + 1, curSum)
            return dp[(i, curSum)]
        return backtrack(0,0)
