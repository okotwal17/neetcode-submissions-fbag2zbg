class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        overlapInterval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if overlapInterval[1] < interval[0]:
                res.append(overlapInterval)
                overlapInterval = interval
            else:
                overlapInterval[0] = min(overlapInterval[0], interval[0])
                overlapInterval[1] = max(overlapInterval[1], interval[1])
        res.append(overlapInterval)
        return res