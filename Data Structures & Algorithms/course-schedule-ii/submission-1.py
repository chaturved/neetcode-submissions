class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[v].append(u)

        top_sort = []
        global_visited = set()

        def dfs(u):
            if u in visited:
                return False
            if u in global_visited:
                return True

            visited.add(u)

            for v in edges[u]:
                if not dfs(v):
                    return False

            visited.remove(u)
            global_visited.add(u)
            top_sort.append(u)
            return True

        for u in range(numCourses):
            visited = set()
            if not dfs(u):
                return []

        return top_sort[::-1]