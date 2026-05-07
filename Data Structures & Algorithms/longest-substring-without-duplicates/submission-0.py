class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = defaultdict(int)
        l = 0
        res = 0

        for r, c in enumerate(s):

            subs[c] += 1

            while subs[c] > 1:
                subs[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

            