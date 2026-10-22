class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        max_cost = 0
        visited = set()
        while heap:
            curr_cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            
            visited.add(u)
            max_cost = max(max_cost, curr_cost)

            for v, cost in adj[u]:
                heapq.heappush(heap, (curr_cost + cost, v))
        
        if len(visited) != n:
            return -1
            
        return max_cost
