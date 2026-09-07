class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        ans = float("inf")

        while L <= R:
            mid = L + (R - L) // 2

            eating_time = 0
            for p in piles:
                eating_time += math.ceil(p/mid)
            
            if eating_time <= h:
                ans = min(ans, mid)
                R = mid - 1
            
            if eating_time > h:
                L = mid + 1

        return ans