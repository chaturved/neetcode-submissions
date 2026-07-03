class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)
        
        visited_global = set()

        def dfs(u):
            if u in visited:
                return False
            if u in visited_global:
                return True
            
            visited.add(u)

            for v in edges[u]:
                if not dfs(v):
                    return False
            
            visited.remove(u)
            visited_global.add(u)
            return True
        
        for u in range(numCourses):
            visited = set()
            if not dfs(u):
                return False
        
        return True