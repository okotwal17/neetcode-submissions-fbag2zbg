class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #             12
        #    1                      5                          10
        #    11                     7                           2
    # 1     5      10           1     5   10                 1  5  10
    # 10    6      1            6     2    NA                1  NA NA
    #                                                    1
    #Amount = 5
    # [0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
    # min(1 + dp[curAmount - coinVal], dp[curAmount])
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, len(dp)):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a - c], dp[a])
        return dp[amount] if dp[amount] != float('inf') else -1