class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            m = target - n

            if m in visited:
                return [visited[m], i]
            
            visited[n] = i