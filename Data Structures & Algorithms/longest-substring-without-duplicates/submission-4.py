class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        ans = 0
        l = 0

        for r in range(len(s)):

            while s[r] in freq:
                freq.remove(s[l])
                l += 1
            freq.add(s[r])
            
            ans = max(ans, r - l + 1)
        return ans