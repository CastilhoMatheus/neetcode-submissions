class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = float('-inf')
        buy = prices[0]

        for p in prices:
            sell = p - buy

            ans = max(ans, sell)
            buy = min(buy, p)
        
        return ans