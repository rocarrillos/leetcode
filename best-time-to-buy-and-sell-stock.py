class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_lowest = max(prices)
        current_highest = min(prices)
        for price in prices:
            if (price <= current_lowest):
                current_lowest = price
                current_highest = price
            if (price > current_highest):
                current_highest = price
                diff = current_highest - current_lowest
                if (max_profit < diff):
                    max_profit = diff
                
        return max_profit
