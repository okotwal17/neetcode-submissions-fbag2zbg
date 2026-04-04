class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        topk = []
        for n in nums:
            count[n]+=1
        for a,v in count.items():
            freq[v].append(a)
        topk = []
        for i in freq[::-1]:
            for e in i:
                if(k==0):
                    break
                topk.append(e)
                k-=1
        return topk


        

