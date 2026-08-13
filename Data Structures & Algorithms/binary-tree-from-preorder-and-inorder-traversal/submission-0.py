# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}

        for i, n in enumerate(inorder):
            hashmap[n] = i
        
        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None
            
            root = TreeNode(preorder[pre_l])
            root_idx = hashmap[preorder[pre_l]]

            size_left = root_idx - in_l

            root.left = dfs(pre_l + 1, pre_l + size_left, in_l, root_idx - 1)
            root.right = dfs(pre_l + size_left + 1, pre_r, root_idx + 1, in_r)

            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)