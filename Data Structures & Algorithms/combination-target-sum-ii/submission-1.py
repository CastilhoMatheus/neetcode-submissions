class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, total, stack):
            if total == target:
                res.append(stack.copy())
                return
            
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                stack.append(candidates[j])
                backtrack(j+1, total + stack[-1], stack)
                stack.pop()
               
        
        backtrack(0, 0, [])
        return res