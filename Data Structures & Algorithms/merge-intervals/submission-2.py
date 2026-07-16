class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        result = []

        for i in range(1, len(intervals)):
            if prev[1] < intervals[i][0]:
                result.append(prev)
                prev = intervals[i]
            else:
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]

        result.append(prev)
        return result

                


