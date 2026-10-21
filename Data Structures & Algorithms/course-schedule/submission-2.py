class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        visited = defaultdict(int)
        def dfs(u):
            if visited[u] == 1:
                return False
            
            if visited[u] == 2:
                return True
                
            visited[u] = 1

            for v in adj[u]:
                if not dfs(v):
                    return False
            
            visited[u] = 2
            return True
        
        for course in range(numCourses):
            if visited[course] == 2:
                continue
            
            if not dfs(course):
                return False
        
        return True