class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        the cost to reach ith floor is
        min(
        the cost to (i - 1)th floor + cost[i - 1]
        the cost to reach (i - 2)th floor + cost[i - 2])
        """
        n = len(cost)

        total_cost = [0] * (n + 1)
        total_cost[0] = 0
        total_cost[1] = 0

        for i in range(2, n + 1):
            total_cost[i] = min(total_cost[i - 1] + cost[i - 1], total_cost[i - 2] + cost[i - 2])
        
        return total_cost[n]



            