class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0 : 1}
        prefix = 0
        res = 0
        for elem in nums:
            prefix += elem
            target = prefix - k
            if target in hashmap:
                res += hashmap[target]
            hashmap[prefix] = 1 + hashmap.get(prefix, 0)
        return res