class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hashmap = {0 : 1}
        curSum = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += hashmap.get(diff, 0)
            hashmap[curSum] = 1 + hashmap.get(curSum, 0)
        return res