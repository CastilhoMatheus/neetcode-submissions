# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):

            if p and not q:
                return False
            
            elif q and not p:
                return False
            
            elif not q and not p:
                return True
            
            elif p.val != q.val:
                return False
            
            
            
            left, right = dfs(p.left, q.left), dfs(p.right, q.right)

            return left and right
        
        return dfs(p, q)

                