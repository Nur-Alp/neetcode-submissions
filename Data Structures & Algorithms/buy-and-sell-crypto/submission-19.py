class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        pointer = 0
        running_min = prices[0]
        for i, n in enumerate(prices):
            if prices[i] < running_min:
                running_min = prices[i]
            if prices[i] - running_min > maxP:
                maxP = prices[i] - running_min
        return maxP