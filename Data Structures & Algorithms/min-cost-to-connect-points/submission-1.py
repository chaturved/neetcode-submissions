class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            
            visited.add(u)
            total_cost += cost
            edges_used += 1
            
            for v in range(n):
                if v not in visited:
                    new_cost = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (new_cost, v))

        return total_cost


        
        
