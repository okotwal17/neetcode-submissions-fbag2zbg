class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda s : s[0])
        res = []
        curInt = intervals[0]
        for i in range(1, len(intervals)):
            if curInt[1] < intervals[i][0]:
                res.append(curInt)
                curInt = intervals[i]
            else:
                curInt = [min(curInt[0], intervals[i][0]), max(curInt[1], intervals[i][1])]
        res.append(curInt)
        return res