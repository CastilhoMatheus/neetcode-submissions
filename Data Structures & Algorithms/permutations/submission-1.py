class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        permutations = self.permute(nums[1:])

        for p in permutations:
            for i in range(len(p) + 1):
                copied = p.copy()
                copied.insert(i, nums[0])
                res.append(copied)

        return res