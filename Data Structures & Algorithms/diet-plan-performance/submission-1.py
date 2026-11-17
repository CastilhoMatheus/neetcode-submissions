class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0

        L = 0
        cur_sum = 0

        for R in range(len(calories)):
            cur_sum += calories[R] 

            while R - L + 1 == k:
                if cur_sum > upper:
                    score += 1
                
                if cur_sum < lower:
                    score -=1

                cur_sum -= calories[L]
                L += 1

               

        return score