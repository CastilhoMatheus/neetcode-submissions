class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        start = 0
        n = len(s)

        for i in range(n):
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > resLen:
                    resLen = r - l
                    start = l

                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > resLen:
                        resLen = r - l
                        start = l

                l -= 1
                r += 1   
        
        return s[start:start+resLen+1]