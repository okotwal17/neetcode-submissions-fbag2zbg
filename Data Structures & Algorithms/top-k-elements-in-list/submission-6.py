class Solution:
    def topKFrequent(self,nums:List[int], k:int) -> List[int]:
        dictionary = {}
        for element in nums:
            if(element in dictionary):
                dictionary[element]+=1
            else:
                dictionary[element]=1

        max_freq = max(dictionary.values())
        buckets = [[] for _ in range(max_freq+1)]

        for k,v in dictionary.items():
            buckets[v].append(k)
        
        res = []
        for i in range(max_freq, 0, -1):
            for n in buckets[i]:
                res.append[n]
                if(len(res) == k):
                    return res

