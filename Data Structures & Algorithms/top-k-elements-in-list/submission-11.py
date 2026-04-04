from collections import defaultdict
class Solution:
    def topKFrequent(self,nums:List[int], k:int) -> List[int]:
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num]+=1

        max_buckets = max(dictionary.values())
        buckets = [[] for a in range(max_buckets + 1)]

        for key,val in dictionary.items():
            buckets[val].append(key)
        
        print(buckets)

        res = []
        for b in reversed(buckets):
            for item in b:
                res.append(item)
                if len(res) == k:
                    return res
        return res


