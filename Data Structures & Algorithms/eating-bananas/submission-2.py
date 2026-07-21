class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        ans = float('inf')

        while L <= R:

            mid = L + (R - L) // 2

            curr_time = 0
            for p in piles:
                curr_time += math.ceil(p/mid)
        
            if curr_time <= h:
                R = mid - 1
                ans = min(ans, mid)
            
            elif curr_time > h:
                L = mid + 1
        
        return ans