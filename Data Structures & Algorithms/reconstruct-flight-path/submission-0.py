class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        
        result = ["JFK"]
        def dfs(u):
            if len(result) == len(tickets) + 1:
                return True
            if u not in adj:
                return False

            temp = adj[u][:]
            for i, v in enumerate(temp):
                adj[u].pop(i)
                result.append(v)

                if dfs(v):
                    return True
                
                adj[u].insert(i, v)
                result.pop()
            
            return False
        
        dfs("JFK")

        return result