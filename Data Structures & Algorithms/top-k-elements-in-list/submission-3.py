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
        print(total)
        for i in freq[::-1]:
            for e in i:
                if(total==0):
                    break
                print(total)
                topk.append(e)
                total-=1
        return topk


        

