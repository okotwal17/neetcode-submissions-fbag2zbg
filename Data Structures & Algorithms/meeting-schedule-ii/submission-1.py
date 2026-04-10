"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 1
        intervals.sort(key = lambda s : s.start)
        for i in range(len(intervals)):
            if i + 1 < len(intervals) and intervals[i].end > intervals[i+1].start:
                res+=1
        return res
            