import pandas as pd

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = pd.Series(prices)
        running_min = prices.cummin()
        profits = prices - running_min
        return int(profits.max())