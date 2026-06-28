class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        start_time = dict()
        heap = []
        for task in tasks:
            if task not in start_time:
                start_time[task] = 0
            else:
                start_time[task] += n + 1
            heap.append((start_time[task], task))
        
        heapq.heapify(heap)

        count_cycles = 0
        while heap:
            start, _ = heapq.heappop(heap)
            count_cycles = max(count_cycles, start) + 1
        
        return count_cycles