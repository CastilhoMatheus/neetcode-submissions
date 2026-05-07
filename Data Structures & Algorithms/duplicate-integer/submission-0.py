class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        duplicates = set()

        for n in nums:
            if n in duplicates:
                return True
            else:
                duplicates.add(n)
        
        return False