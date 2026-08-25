"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        1   5
         2   6
          3   7
           4   8
            5   9
             6  9
           
        
        """
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        res = 0
        s, e = 0, 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                res += 1
                s += 1
            else:
                s += 1
                e += 1
        return res