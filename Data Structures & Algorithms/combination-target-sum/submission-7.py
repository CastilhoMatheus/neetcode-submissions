class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, s, stack):
            if i >= len(nums):
                return
            if s == target:
                res.append(stack.copy())
                return
            
            if s > target:
                return
            
            n = nums[i]
            s += n
            stack.append(n)
            backtrack(i, s, stack)
            last = stack.pop()
            s -= last
            backtrack(i+1, s, stack)


        backtrack(0, 0, [])
        return res