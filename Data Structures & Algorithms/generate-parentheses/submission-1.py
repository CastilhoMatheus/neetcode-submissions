class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(op, cl, path):
            if op == cl and op == n:
                res.append(path)

            if op < n:
                backtrack(op + 1, cl, path + "(")
            
            if cl < op:
                backtrack(op, cl + 1, path + ")")
        
        backtrack(0, 0, "")
        return res