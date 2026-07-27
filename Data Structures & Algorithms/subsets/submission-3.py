class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, array):
            if i >= len(nums):
                res.append(array)
                return

            backtrack(i + 1, array)
            backtrack(i + 1, [nums[i]] + array)

        backtrack(0, [])
        return res
