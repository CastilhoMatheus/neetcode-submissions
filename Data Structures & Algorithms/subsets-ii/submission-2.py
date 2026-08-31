class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, stack):
            res.append(stack.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                stack.append(nums[j])
                backtrack(j + 1, stack)
                stack.pop()
                

        backtrack(0, [])
        return res