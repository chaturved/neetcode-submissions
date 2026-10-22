class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, p in flights:
            adj[u].append((v, p))
        
        heap = [(0, src, 0)]
        visited = set()

        while heap:
            curr_cost, u, stops = heapq.heappop(heap)
            if (u, stops) in visited:
                continue
            
            visited.add((u, stops))

            if stops > k + 1:
                continue
            
            if u == dst:
                return curr_cost
            
            for v, cost in adj[u]:
                heapq.heappush(heap, (curr_cost + cost, v, stops + 1))
        
        return -1