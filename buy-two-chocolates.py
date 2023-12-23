class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_choccies = sorted(prices)
        min_choccy_price = sorted_choccies[0] + sorted_choccies[1]
        if money - min_choccy_price >= 0:
            return money - min_choccy_price
        return money