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
        [0, 7], [2, 5], [3, 6] [7, 10], [5, 11]
        [0, 7], [2, 5], [3, 6], [5, 11], [7, 10]
        """
        intervals.sort(key=lambda x: x.start)
        heap = []
        min_rooms = 0
        for interval in intervals:
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            min_rooms = max(min_rooms, len(heap))
        
        return min_rooms


            
            

        
