class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(u):
            if u in visited:
                return

            visited.add(u)
            for v in adj[u]:
                dfs(v)
        
        count = 0
        for u in range(n):
            if u in visited:
                continue
            
            dfs(u)
            count += 1
        
        return count

            