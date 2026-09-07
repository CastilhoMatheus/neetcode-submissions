class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        cur_sum = 0
        res = 0

        for n in nums:
            cur_sum += n
            diff = cur_sum - k
        
            res += prefixSums[diff]

            prefixSums[cur_sum] += 1
        
        return res