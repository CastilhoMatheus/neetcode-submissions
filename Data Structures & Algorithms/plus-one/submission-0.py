class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""

        for n in digits:
            s += str(n)

        p = int(s) + 1

        res = deque([])

        while p:
            f = p % 10
            p //= 10
            res.appendleft(f)
    
        return list(res)