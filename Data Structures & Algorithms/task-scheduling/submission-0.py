class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [] # tasks count

        for v in count.values():
            heapq.heappush(maxHeap, -v)

        time = 0

        q = deque() #[-v, idleTime]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            
            else:
                count = 1 + heapq.heappop(maxHeap)
            
                if count:
                    q.append([count, time + n])
                
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
