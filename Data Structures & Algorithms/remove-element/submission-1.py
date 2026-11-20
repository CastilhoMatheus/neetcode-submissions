class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            if nums[L] == val:
                nums[L] = nums[R]
                R -= 1
            else:
                L += 1
        
        return L