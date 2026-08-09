class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = float('inf')
        for price in prices:
            min_buy_price = min(min_buy_price, price)
            max_profit = max(max_profit, price - min_buy_price)
        
        return max_profit

