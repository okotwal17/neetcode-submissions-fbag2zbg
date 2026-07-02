from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Get freq of all unique numbers
        counts = dict(Counter(nums))
        maxFreq  = max(counts.values())
        buckets = [[] for _ in range(maxFreq + 1)]
        for key, v in counts.items():
            buckets[v].append(key)
        idx = len(buckets) - 1
        res = []
        #Go throught each of the buckets reverse order and then go throguh their arrays
        for arr in reversed(buckets):
            for i in reversed(arr):
                if k > 0:
                    res.append(i)
                    k-=1
                else:
                    break
        return res
