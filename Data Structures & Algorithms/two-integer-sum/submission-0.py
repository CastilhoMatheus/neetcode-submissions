class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)

        for i in range(n):
            aux = target - nums[i]

            if aux in hashmap:
                return [hashmap.get(aux), i]
            hashmap[nums[i]] = i
    

