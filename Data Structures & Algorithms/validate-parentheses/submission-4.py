class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            
            else:
                pair = pairs[c]

                if not stack or stack[-1] != pair:
                    return False
                
                stack.pop()
        
        return True if len(stack) < 1 else False