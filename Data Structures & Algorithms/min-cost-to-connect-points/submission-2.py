class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        union_find = UnionFind(n)

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        heapq.heapify(edges)

        total_cost = 0
        edges_used = 0
        while edges_used < n - 1:
            cost, u, v = heapq.heappop(edges)
            if union_find.union(u, v):
                total_cost += cost
                edges_used += 1

        return total_cost


class UnionFind:
    def __init__(self, n):
        self.parent = [u for u in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False
        self.parent[parent_v] = parent_u
        return True