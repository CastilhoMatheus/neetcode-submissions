class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i ,n in enumerate(nums):
            missing = missing ^ i        
            missing = missing ^ n

        return missing
            
