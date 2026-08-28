"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([s.start for s in intervals])
        end = sorted([s.end for s in intervals])
        s, e = 0, 0
        current, res = 0,0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                current += 1
                s += 1
            else:
                current -= 1
                e += 1
            res = max(res, current)
        return res