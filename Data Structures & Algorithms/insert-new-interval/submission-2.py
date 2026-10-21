class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid - 1
        
        intervals.insert(l, newInterval)

        res = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                res.append(prev)
                prev = interval
        
        res.append(prev)
        return res