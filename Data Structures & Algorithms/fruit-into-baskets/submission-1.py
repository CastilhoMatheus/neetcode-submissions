class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        L = 0
        basket = defaultdict(int) # 2 at most
        ans = 0

        for R in range(len(fruits)):
            basket[fruits[R]] += 1
            
            while len(basket) > 2:
                basket[fruits[L]] -= 1
                if basket[fruits[L]] == 0:
                    del basket[fruits[L]]
                L += 1
            
            ans = max(ans, R - L + 1)
        
        return ans
