class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])

        n = len(points)
        heap = [(0, tuple(points[0]))]
        visited = set()
        total_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)

            if u in visited:
                continue

            visited.add(u)
            total_cost += cost

            if len(visited) == n:
                return total_cost

            for v in points:
                v = tuple(v)
                if v not in visited:
                    heapq.heappush(heap, (distance(u, v), v))

        return total_cost