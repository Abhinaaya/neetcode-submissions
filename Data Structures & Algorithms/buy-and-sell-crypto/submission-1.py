class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy=prices[0]
        max_profit=0
        for i in range(len(prices)):
            profit=prices[i]-min_buy
            max_profit=max(max_profit,profit)
            min_buy=min(prices[i],min_buy)
        return max_profit
        
        