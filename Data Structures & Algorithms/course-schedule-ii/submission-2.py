class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for v, u in prerequisites:
            adj[u].append(v)
        
        visited_states = defaultdict(int)
        postorder = []

        def dfs(u):
            if visited_states[u] == 1:
                return False
            
            if visited_states[u] == 2:
                return True
            
            visited_states[u] = 1

            for v in adj[u]:
                if not dfs(v):
                    return False
            
            postorder.append(u)
            visited_states[u] = 2
            return True
            

        for u in range(numCourses):
            if visited_states[u] == 2:
                continue
            
            if not dfs(u):
                return []
        
        return postorder[::-1]
