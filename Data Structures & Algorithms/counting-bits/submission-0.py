class Solution:
    def countOnes(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            
            n = n >> 1
        
        return count

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(len(ans)):
            ans[i] = self.countOnes(i)
        
        return ans