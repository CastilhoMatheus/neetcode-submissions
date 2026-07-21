class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in matrix:
            L, R = 0, len(r) - 1 

            while L <= R:
                mid = L + (R - L) // 2

                if r[mid] > target:
                    R = mid - 1
                
                elif r[mid] < target:
                    L = mid + 1
                
                else:
                    return True
        
        return False