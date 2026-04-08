class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(remainingCoins):
            if remainingCoins == 0:
                return 0
            if remainingCoins in cache:
                return cache[remainingCoins]
            
            res = 1e9
            for coin in coins:
                if remainingCoins - coin >=0:
                    print(remainingCoins)
                    res = min(res, 1 + dfs(remainingCoins - coin))
            cache[remainingCoins] = res
            return res
        ret = dfs(amount)
        return ret if ret < 1e9 else -1