class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        L = 0
        ans = 0

        for R in range(len(s)):
            while s[R] in ch:
                ch.remove(s[L])
                L += 1
            
            ch.add(s[R])
            ans = max(ans, 1 + R - L)

        return ans