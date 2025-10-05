class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for j in prices:
            if min_price <= j:
                max_profit += j - min_price
            min_price = j
        return max_profit