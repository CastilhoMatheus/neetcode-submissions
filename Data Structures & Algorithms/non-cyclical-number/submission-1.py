class Solution:
    def get_next(self, number: int) -> int:
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum

    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n
        while curr != 1 and curr not in seen:
            seen.add(curr)
            curr = self.get_next(curr)
        return curr == 1