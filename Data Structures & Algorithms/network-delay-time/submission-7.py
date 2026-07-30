class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        min_heap = [(0, k)]
        visited = set()
        time_taken = float('-inf')

        while min_heap:
            curr_t, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)

            time_taken = curr_t

            for v, t in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (curr_t + t, v))
        
        if len(visited) != n:
            return -1
        
        return time_taken
        
