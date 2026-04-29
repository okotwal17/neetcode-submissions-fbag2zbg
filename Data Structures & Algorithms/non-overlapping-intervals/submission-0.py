class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda s : s[0]) #Sorting by start time
        count = 0
        curInt = intervals[0]
        for i in range(1, len(intervals)):
            if curInt[1] > intervals[i][0]:
                curInt = [max(curInt[0], intervals[i][0]), min(curInt[1], intervals[i][1])]
                count+=1
            else:
                curInt = intervals[i]
        return count