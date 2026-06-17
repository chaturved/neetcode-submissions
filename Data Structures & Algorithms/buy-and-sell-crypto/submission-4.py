class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while left <= right and right < len(prices):
            if prices[left] <= prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1
            else:
                left = right
        
        return max_profit