class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minsofar = prices[0]
        for i in prices:
            profit = i - minsofar
            maxprofit = max(profit, maxprofit)
            minsofar = min(i, minsofar)

        return maxprofit
