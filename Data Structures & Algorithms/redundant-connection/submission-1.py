class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        redundant_connections = set()
        for u, v in edges:
            if not union_find.union(u, v):
                return [u, v]
        
        return -1


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False
        
        self.parent[parent_u] = parent_v
        return True
    