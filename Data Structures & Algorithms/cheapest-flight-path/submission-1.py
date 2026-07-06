class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        
        min_heap = [(0, src, 0)]
        visited = set()
        
        while min_heap:
            curr_cost, u, curr_k = heapq.heappop(min_heap)
            
            if u == dst and curr_k <= k + 1:
                return curr_cost
            
            if curr_k == k + 1:
                continue
            
            if (u, curr_k) in visited:
                continue
                
            visited.add((u, curr_k))
            
            for v, cost in adj[u]:
                if (v, curr_k + 1) not in visited:
                    heapq.heappush(min_heap, (curr_cost + cost, v, curr_k + 1))
        
        return -1