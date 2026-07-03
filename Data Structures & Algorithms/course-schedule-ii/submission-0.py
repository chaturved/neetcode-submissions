class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)

        
        top_sort = []
        global_visited = set()
        
        def dfs(u):
            if u in visited:
                return False
            
            visited.add(u)

            if u in global_visited:
                return True

            for v in edges[u]:
                if not dfs(v):
                    return False
            
            visited.remove(u)
            
            top_sort.append(u)
            global_visited.add(u)

            return True
        
        for u in range(numCourses):
            visited = set()
            if not dfs(u):
                return []
            
        return top_sort
