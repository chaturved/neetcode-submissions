class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()
        while heap:
            curr_cost, u = heapq.heappop(heap)

            if u in visited:
                continue
            
            visited.add(u)

            if len(visited) == n:
                return curr_cost

            for v, edge_cost in adj[u]:
                if v not in visited:
                    heapq.heappush(heap, (curr_cost + edge_cost, v))

        return -1
        
