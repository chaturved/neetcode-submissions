class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        queue = deque()
        for u in range(numCourses):
            if indegree[u] == 0:
                queue.append(u)
        
        taken = 0
        while queue:
            u = queue.popleft()
            taken += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return taken == numCourses
