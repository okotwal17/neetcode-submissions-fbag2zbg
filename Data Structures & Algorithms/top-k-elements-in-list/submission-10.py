class Solution:
    def topKFrequent(self,nums:List[int], k:int) -> List[int]:
        #1. Filling up the dictionary with the frequencies
        dictionary = {}
        for elements in nums:
            if(elements in dictionary):
                dictionary[elements]+=1
            else:
                dictionary[elements]=1
        #2. Create the buckets
        maxFreq = max(dictionary.values())
        buckets = [[] for a in range(0,maxFreq+1)]

        #3. Fill the buckets
        for key, value in dictionary.items():
            buckets[value].append(key)
        
        #4. Get the top k elements
        res = []
        for i in range(maxFreq,0,-1):
            for n in buckets[i]:
                res.append(n)
                if(len(res)==k):
                    return res

