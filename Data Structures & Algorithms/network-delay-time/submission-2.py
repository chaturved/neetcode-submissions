class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = defaultdict()
        queue = deque()
        queue.append((k, 0))
        visited[k] = 0

        while queue:
            node, cost = queue.popleft()
            for nei, nei_cost in adj[node]:
                new_cost = cost + nei_cost
                if nei in visited and visited[nei] <= new_cost:
                    continue
                visited[nei] = new_cost
                queue.append((nei, new_cost))
        
        if len(visited) != n:
            return -1
        
        return max(visited.values())