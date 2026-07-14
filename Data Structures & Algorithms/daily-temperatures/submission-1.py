class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [val, index]
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                index = stack[-1][1]
                result[index] = i - index 
                stack.pop()
            
            stack.append([t, i])

        return result 

