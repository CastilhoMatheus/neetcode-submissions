class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        og = x
        rev = 0

        while x > 0:
            most_right = x % 10
            rev = rev * 10 + most_right
            x = x // 10
        
        return og == rev