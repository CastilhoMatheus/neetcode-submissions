class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total_sum = 0

        for c in operations:
            if c == "+":
                cur = res[-1] + res[-2]
                res.append(cur)
                total_sum += cur
            
            elif c == "C":
                cur = res.pop()
                total_sum -= cur
            
            elif c == "D":
                cur = res[-1] * 2
                res.append(cur)
                total_sum += cur
            
            else:
                val = int(c)
                res.append(val)
                total_sum += val

        return total_sum