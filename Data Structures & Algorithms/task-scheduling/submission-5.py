class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        heap = list(freq.values())
        heapq.heapify_max(heap)

        queue = deque()
        curr_time = 0

        while heap or queue:
            if queue and queue[0][0] <= curr_time:
                _, count = queue.popleft()
                heapq.heappush_max(heap, count)
            
            if heap:
                count = heapq.heappop_max(heap)
                if count > 1:
                    queue.append((curr_time + n + 1, count - 1))

            curr_time += 1
        
        return curr_time
            