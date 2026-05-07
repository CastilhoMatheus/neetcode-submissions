class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def backtrack(remaining):

            if not remaining:
                res.append(stack.copy())
                return
            
            for i, n in enumerate(remaining):
                stack.append(n)
                backtrack(remaining[:i] + remaining[i+1:])
                stack.pop()
        
        backtrack(nums)
        return res
            