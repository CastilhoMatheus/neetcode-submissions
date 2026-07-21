class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        if nums[L] <= nums[R]:
            return nums[L]

        while L <= R:

            mid = L + (R - L) // 2

            if nums[mid] < nums[(mid - 1) % n]:
                return nums[mid]
            
            elif nums[mid] >= nums[0]:
                L = mid + 1
            
            else:
                R = mid - 1
