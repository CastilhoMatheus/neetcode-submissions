class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if nums[i] > 0:
                break;

            if i > 0 and nums[i] == nums[i-1]:
                continue;
            
            L, R = i + 1, n-1

            while L < R:
                tsum = nums[i] + nums[L] + nums[R]

                if tsum > 0:
                    R -= 1
                
                elif tsum < 0:
                    L += 1

                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while nums[L] == nums[L-1] and L < R:
                        L += 1

        return ans
           