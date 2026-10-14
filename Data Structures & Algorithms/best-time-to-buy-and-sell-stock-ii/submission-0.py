class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        total_profit = 0
        while i < len(prices):
            j = i
            while j < len(prices) - 1 and prices[j] <= prices[j + 1]:
                j += 1

            curr_profit = max(0, prices[j] - prices[i])
            total_profit += curr_profit
            i = j + 1

        return total_profit