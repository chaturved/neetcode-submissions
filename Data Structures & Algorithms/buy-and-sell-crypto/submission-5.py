class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for current_price in prices:
            max_profit = max(max_profit, current_price - buy)
            buy = min(buy, current_price)
        
        return max_profit