class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        L = 0
        window = defaultdict(int)
        ans = float('inf')

        for R in range(len(blocks)):
            window[blocks[R]] += 1
            
            while R - L + 1 == k:
                print(ans)
                ans = min(ans, window["W"])
                window[blocks[L]] -= 1
                L += 1
            
        
        return ans