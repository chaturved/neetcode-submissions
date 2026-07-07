class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        the cost to reach ith floor is
        min(
        the cost to (i - 1)th floor + cost[i - 1]
        the cost to reach (i - 2)th floor + cost[i - 2])
        """
        n = len(cost)

        total_cost_prev = 0
        total_cost_curr = 0

        for i in range(2, n + 1):
            total_cost_curr, total_cost_prev = min(total_cost_curr + cost[i - 1], total_cost_prev + cost[i - 2]), total_cost_curr
        
        return total_cost_curr



            