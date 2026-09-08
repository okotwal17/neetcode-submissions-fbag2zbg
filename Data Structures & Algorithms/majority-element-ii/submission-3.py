class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            if len(hashmap) > 2:
                hashmapDupe = hashmap.copy()
                for k, v in hashmapDupe.items():
                    hashmap[k] = v - 1
                    if not hashmap[k]:
                        del hashmap[k]
        res = []
        for k,v in hashmap.items():
            if nums.count(k) > len(nums) // 3:
                res.append(k)
        return res


        
        
