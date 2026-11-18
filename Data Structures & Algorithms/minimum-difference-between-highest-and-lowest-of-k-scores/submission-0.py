class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        L, R = 0, k - 1

        while L <= R and R < len(nums):
            res = min(res, nums[R] - nums[L])

            L += 1
            R += 1

        return res