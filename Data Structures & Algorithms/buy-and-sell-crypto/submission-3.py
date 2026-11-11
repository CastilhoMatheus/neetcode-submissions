class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        profit = float('-inf')

        for p in prices:
            
            profit = max(profit, p - buy)
            buy = min(buy, p)

        return profit