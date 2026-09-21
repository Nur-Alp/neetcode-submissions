import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = np.array(prices)
        running_min = np.minimum.accumulate(prices)
        profits = prices - running_min
        return int(np.max(profits))