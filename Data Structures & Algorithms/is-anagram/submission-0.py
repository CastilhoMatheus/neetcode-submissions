class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}

        for l in s:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1


        for l in t:
            if (l not in letters or letters[l] < 1):
                return False
            else:
                letters[l] -= 1

        return True