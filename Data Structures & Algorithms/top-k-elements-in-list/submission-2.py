class Solution:
    from collections import defaultdict
    def topKFrequent(self,nums:List[int], k:int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Create buckets (list of lists)
        max_freq = max(freq_map.values())
        buckets = [[] for _ in range(max_freq + 1)]

        # Step 3: Fill the buckets
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 4: Collect top K elements
        res = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
