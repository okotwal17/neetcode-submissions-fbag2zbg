class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Use the hashamp to see if there is a chopped off bit in there.  
        res = 0
        hashmap = {0 : 1}
        prefixSum = 0
        for num in nums:
            prefixSum += num
            print(prefixSum, num)
            target = prefixSum - k
            if target in hashmap:
                res += hashmap[target]
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1
            print(res)
        return res
