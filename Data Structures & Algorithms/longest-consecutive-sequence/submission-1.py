class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        ans = 0

        for n in nums:
            if n-1 not in numSet:
                count = 1

                while n+1 in numSet:
                    count += 1
                    n = n + 1
                
                ans = max(ans, count)
        
        return ans
                
