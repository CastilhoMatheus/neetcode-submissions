class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def backtrack(i, summ, stack):
            if summ == target:
                res.append(stack.copy())
                return
            

            if i < len(nums) and summ <= target:
                stack.append(nums[i])
                backtrack(i, summ + nums[i], stack)
                stack.pop()
                backtrack(i + 1, summ, stack)
            

        res = []

        backtrack(0, 0, [])
        return res