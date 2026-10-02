class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            return sub ==sub[::-1]

        def backtrack(start, stack):
            if start == len(s):
                res.append(stack[:])
                return
            
            for end in range(start, len(s)):
                sub = s[start:end + 1]
                if is_palindrome(sub):
                    stack.append(sub)
                    backtrack(end + 1, stack)
                    stack.pop()

        backtrack(0, [])

        return res