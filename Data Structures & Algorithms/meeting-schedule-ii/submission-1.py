"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, x.end))

        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)
        
        l, r = 0, 0
        max_count, count = 0, 0
        while l < len(start):
            if start[l] < end[r]:
                count += 1
                l += 1
            else:
                count -= 1
                r += 1
            max_count = max(max_count, count)
        
        return max_count
        


