class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(remainingCoins):
            if remainingCoins in cache:
                return cache[remainingCoins]
            if remainingCoins == 0:
                return 0
            res = 1e9
            for i in coins:
                if remainingCoins - i >=0:
                    res = min(res, 1 + dfs(remainingCoins - i))
            cache[remainingCoins] = res
            return res
        ret = dfs(amount)
        return ret if ret < 1e9 else -1