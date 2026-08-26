class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_right = (a >> i) & 1
            b_right = (b >> i) & 1

            sum_bit = a_right ^ b_right ^ carry

            carry = (a_right + b_right + carry) >= 2

            if sum_bit:
                res |= (1 << i)
            
            if res > 0x7FFFFFFF:
                res = ~(res ^ mask)

        return res