class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        low,high = 0,1
        n = len(prices)
        while high < n:
            if prices[low]<prices[high]:
                profit = prices[high]-prices[low]
                if profit>maxPro:
                    maxPro = profit
            else:
                low = high
            high+=1
        return maxPro