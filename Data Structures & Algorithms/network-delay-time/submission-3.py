class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (0, k))
        total_cost = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
                
            visited.add(node)
            total_cost = max(total_cost, cost)

            for nei, nei_cost in adj[node]:
                heapq.heappush(min_heap, (cost + nei_cost, nei))
        
        if len(visited) != n:
            return -1

        return total_cost