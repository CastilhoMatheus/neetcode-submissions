class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = float("-inf")

        for p in prices:
            profit = p - buy

            if profit > ans:
                ans = profit

            buy = min(buy, p)

        return ans