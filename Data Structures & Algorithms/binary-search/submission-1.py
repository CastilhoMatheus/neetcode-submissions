class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)

        while L < R:
            
            mid = L + (R - L) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid
            
        return -1
