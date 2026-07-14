class Solution:
    def calc(self, A, B, operator):
        a = int(A)
        b = int(B)

        if operator == "*":
            return a * b
        elif operator == "/":
            return int(b / a)
        elif operator == "+":
            return a + b
        else:
            return b - a
    
    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        operators = ["*", "-", "/",  "+"]

        for t in tokens:
            if t in operators:
                a, b = values.pop(), values.pop()

                summ = self.calc(a, b, t)
                values.append(str(summ))
            else:
                values.append(t)
        
        return int(values[-1])