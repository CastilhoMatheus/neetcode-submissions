"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        res, count = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1

            else:
                count -= 1
                e += 1
            
            res = max(res, count)
        
        return res