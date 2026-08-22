class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #O(n) memory solution
        #
        #O(1) memory solution
        intervals.sort(key = lambda x : x[0])
        res = 0
        endInterval = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if endInterval <= interval[0]:
                endInterval = interval[1]
            else:
                res += 1
                endInterval = min(endInterval, interval[1])
        return res 