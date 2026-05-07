# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levelOrder = []
        q = deque()
        q.append(root)

        while q:
            level = len(q)
            cur_level = []

            for i in range(level):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    cur_level.append(node.val)
            
            if cur_level:
                levelOrder.append(cur_level)
        
        res = []
        for level in levelOrder:
            res.append(level[-1])
        
        return res