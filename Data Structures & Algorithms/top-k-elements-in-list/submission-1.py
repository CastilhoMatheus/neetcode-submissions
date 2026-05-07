class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        items_arr = list(count.items())

        items_arr.sort(reverse=True, key=lambda d: d[1])
        
        ans = []
        for i in range(k):
            ans.append(items_arr[i][0])

        return ans