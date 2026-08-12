class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0]<=newInterval[0]<=interval[1] or interval[0]<=newInterval[1]<=interval[1] or newInterval[0]<=interval[0]<=newInterval[1] or newInterval[0]<=interval[1]<=newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                res.append(newInterval)
                return res + intervals[i:]
        res.append(newInterval)
        return res