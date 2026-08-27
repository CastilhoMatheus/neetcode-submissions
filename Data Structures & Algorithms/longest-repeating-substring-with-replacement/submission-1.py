class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0

        res = 0
        freq = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            freq = max(freq, count[s[R]])

            while (1 + R - L) - freq > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, 1 + R - L)

        
        return res