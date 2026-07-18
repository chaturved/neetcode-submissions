class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        result = [-1] * len(queries)
        i, n = 0, len(intervals)

        for query_index, query in sorted(enumerate(queries), key=lambda x: x[1]):
            while min_heap and min_heap[0][1] + min_heap[0][0] - 1 < query:
                heapq.heappop(min_heap)
            
            
            while i < n and intervals[i][0] <= query:
                start, end = intervals[i]
                if end >= query:
                    heapq.heappush(min_heap, (end - start + 1, start, i))
                i += 1

            if min_heap:
                result[query_index] = min_heap[0][0]

        return result