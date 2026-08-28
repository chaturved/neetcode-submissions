class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u, p):
            total_time = 0
            for v in adj[u]:
                if v == p:
                    continue
                
                time_taken = dfs(v, u)

                if hasApple[v] or time_taken > 0:
                    total_time += time_taken + 2
            
            return total_time
        
        return dfs(0, -1)