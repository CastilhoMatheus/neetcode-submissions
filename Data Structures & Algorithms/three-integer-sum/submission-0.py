class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        if nums[0] > 0: return res

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue

            l, r = i + 1, len(nums) - 1
            
            print(i,l,r)

            while l < r:
                cur_sum = n + nums[l] + nums[r]
                
                if cur_sum < 0:
                    l += 1
                
                elif cur_sum > 0:
                    r -= 1
                
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res