class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ordered_arr =[]
        
        for key, v in count.items():
            ordered_arr.append((key,v))
        
        ordered_arr.sort(key = lambda p: p[1], reverse=True)
        
        ans = []
        i = 0
        while k:
            ans.append(ordered_arr[i][0])
            i+=1
            k-=1

        return ans