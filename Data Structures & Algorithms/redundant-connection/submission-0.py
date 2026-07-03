class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        cycle = set()
        cycle_start = -1

        def dfs(u, p):
            nonlocal cycle_start
            if u in visited:
                cycle_start = u
                return True
            
            visited.add(u)

            for v in adj[u]:
                if v == p:
                    continue
                if dfs(v, u):
                    if cycle_start != -1:
                        cycle.add(v)
                    if u == cycle_start:
                        cycle_start = -1
                    return True

            return False
        
        dfs(1, -1)

        for u, v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u, v]
        
        return []
        
        