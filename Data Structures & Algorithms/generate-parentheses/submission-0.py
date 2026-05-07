class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []     
        res = []

        def backtrack(o, c):
            if len(path)== 2 * n:
                copy = path
                res.append(''.join(path))
                return

            if o < n:
                path.append('(')
                backtrack(o + 1, c)
                path.pop()
            
            if c < o:
                path.append(')')
                backtrack(o, c + 1)
                path.pop()
        
        backtrack(0, 0)
        return res