class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for u, v, p in flights:
                temp[v] = min(temp[v], prices[u] + p)
            prices = temp
        
        if prices[dst] == float('inf'):
            return -1 

        return prices[dst]
