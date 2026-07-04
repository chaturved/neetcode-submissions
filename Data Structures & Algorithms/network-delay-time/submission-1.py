class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = defaultdict()

        def dfs(node, cost):
            if node in visited and cost >= visited[node]:
                return
            
            visited[node] = cost

            for nei, nei_cost in adj[node]:
                dfs(nei, cost + nei_cost)
        
        dfs(k, 0)

        if len(visited) != n:
            return -1
        
        return max(visited.values())
