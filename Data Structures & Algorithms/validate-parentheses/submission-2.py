class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:

            if c not in pairs:
                stack.append(c)

            elif stack and pairs[c] == stack[-1]:
                stack.pop()
            
            else: return False
        
        return True if not len(stack) else False