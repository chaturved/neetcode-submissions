class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        postorder = []
        visited = defaultdict(int)

        def dfs(u):
            if visited[u] == 2:
                return True
            
            if visited[u] == 1:
                return False
            
            visited[u] = 1

            for v in adj[u]:
                if not dfs(v):
                    return False
            
            postorder.append(u)
            visited[u] = 2
            return True
        
        for u in range(numCourses):
            if not dfs(u):
                return []
        
        top_sort = postorder[::-1]
        return top_sort
            