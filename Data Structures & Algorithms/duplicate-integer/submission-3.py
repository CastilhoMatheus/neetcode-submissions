class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}

        for n in nums:
            if n in visited:
                return True
            
            visited[n] = True
        
        return False