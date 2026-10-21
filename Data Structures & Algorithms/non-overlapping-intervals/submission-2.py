class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        overlapping_intervals = 0
        for interval in intervals[1:]:
            if prev[1] > interval[0]:
                prev[1] = min(prev[1], interval[1])
                overlapping_intervals += 1
            else:
                prev = interval

        return overlapping_intervals
        
