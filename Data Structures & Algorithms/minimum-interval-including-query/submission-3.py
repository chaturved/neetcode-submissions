class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        intervals.sort()
        heap = []
        res = {}
        i = 0
        for query in sorted(queries):
            while i < n and intervals[i][0] <= query:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            res[query] = heap[0][0] if heap else -1
        
        return [res[query] for query in queries]
            

            
            
