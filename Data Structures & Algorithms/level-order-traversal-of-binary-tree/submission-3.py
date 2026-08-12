# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        q = deque([[root]])

        while q:
            level = q.popleft()

            children = []
            cur = []
            for node in level:
                cur.append(node.val)

                if node.left:
                    children.append(node.left)
                
                if node.right:
                    children.append(node.right)
            
            if children:
                q.append(children)
            ans.append(cur)
        
        return ans