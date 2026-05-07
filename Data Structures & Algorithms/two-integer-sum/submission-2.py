class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {} # val = index

        for i, n in enumerate(nums):
            x = target - n

            if x in idx_map:
                return [idx_map[x], i]
            
            idx_map[n] = i