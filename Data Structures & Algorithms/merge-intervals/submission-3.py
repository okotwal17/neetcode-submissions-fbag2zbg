class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergeInterval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if mergeInterval[1] < interval[0]:
                res.append(mergeInterval)
                mergeInterval = interval
            else:
                mergeInterval[0] = min(mergeInterval[0], interval[0])
                mergeInterval[1] = max(mergeInterval[1], interval[1])
        res.append(mergeInterval)
        return res
            