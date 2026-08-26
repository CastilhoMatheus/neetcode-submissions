class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = 0
        for i in range(len(nums)):
            cur = nums[i] ^ cur
        
        return cur