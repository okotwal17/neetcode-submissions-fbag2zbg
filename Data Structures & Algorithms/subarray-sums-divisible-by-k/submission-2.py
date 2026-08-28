class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #4 --> {4 : 1}{0 : 1}
        hashmap = {0 : 1}
        res = 0
        prefix = 0
        for num in nums:
            prefix += num
            key = prefix % k
            res += hashmap.get(key, 0)
            hashmap[key] = 1 + hashmap.get(key, 0)
        return res