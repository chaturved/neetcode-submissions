class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        memo = {}
        
        def dfs(u):
            if u in memo:
                return memo[u]
            
            result = set()
            for v in adj[u]:
                result.add(v)
                result |= dfs(v)
            
            memo[u] = result
            return result
        
        for u in range(numCourses):
            dfs(u)
        
        return [v in memo[u] for u, v in queries]