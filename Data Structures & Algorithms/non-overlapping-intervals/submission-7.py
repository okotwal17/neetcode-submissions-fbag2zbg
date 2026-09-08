class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        mergeInt = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if mergeInt[1] > intervals[i][0]:
                mergeInt[1] = min(intervals[i][1], mergeInt[1])
                res += 1
            else:
                mergeInt = intervals[i]
        return res