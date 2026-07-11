class Solution:
    def calcArea(self, smallestPillar, i, j):
        return smallestPillar * (j - i)

    def maxArea(self, heights: List[int]) -> int:
        
        container = 0
        i, j = 0, len(heights) - 1

        while i <= j:
            volume = self.calcArea(min(heights[i], heights[j]), i, j)

            container = max(container, volume)

            if heights[i] > heights[j]:
                j -= 1
            
            else:
                i += 1
            
        
        return container

