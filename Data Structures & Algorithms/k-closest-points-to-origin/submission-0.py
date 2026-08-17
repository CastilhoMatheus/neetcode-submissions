class Solution:

    def calculateDistance(self, x, y):
        return math.sqrt(((0 - x) * (0-x)) + ((0 - y) * (0-y)))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # triple (dist, x, y)

        for p in points:
            x, y = p
            heapq.heappush(heap, (self.calculateDistance(x, y), x, y))
    
        ans = []

        while heap and k:
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
            k-= 1
            
        return ans