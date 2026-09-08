class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda d: d[0])
            
        cur_interval = intervals[0]
        for i in range(len(intervals)-1):
            start_next, end_next = intervals[i+1][0], intervals[i+1][1]
            
            if cur_interval[1] >= start_next:
                cur_interval[1] = max(end_next, cur_interval[1])
            else:
                ans.append(cur_interval)
                if i < len(intervals)-1:
                    cur_interval = intervals[i+1]

        ans.append(cur_interval)
        return ans