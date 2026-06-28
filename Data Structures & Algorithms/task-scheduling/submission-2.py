class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        heap = [(count, task) for task, count in freq.items()]
        heapq.heapify_max(heap)

        queue = deque()
        count_cycles = 0
        while heap or queue:
            if queue and queue[0][0] == count_cycles:
                available_at, count, task = queue.popleft()
                heapq.heappush_max(heap, (count, task))
            
            if heap:
                count, task = heapq.heappop_max(heap)
                count_cycles += 1
                if count - 1 > 0:
                    queue.append((count_cycles + n, count - 1, task))
            else:
                count_cycles = queue[0][0]
        
        return count_cycles